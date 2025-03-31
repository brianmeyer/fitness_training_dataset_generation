import json
import os
import re
from groq import Groq
from tqdm import tqdm
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
from collections import deque
from datetime import datetime, timedelta

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Rate limiting settings
RPM_LIMIT = 30  # requests per minute
REQUESTS_WINDOW = deque(maxlen=RPM_LIMIT)
MIN_REQUEST_INTERVAL = 60 / RPM_LIMIT  # minimum seconds between requests

class CheckpointManager:
    def __init__(self, checkpoint_file):
        self.checkpoint_file = checkpoint_file
        self.last_processed_line = self._load_checkpoint()
    
    def _load_checkpoint(self):
        """Load the last processed line number from checkpoint file"""
        try:
            if os.path.exists(self.checkpoint_file):
                with open(self.checkpoint_file, 'r') as f:
                    checkpoint_data = json.load(f)
                    return checkpoint_data.get('last_processed_line', 0)
        except Exception as e:
            print(f"Error loading checkpoint: {e}")
        return 0
    
    def save_checkpoint(self, line_number):
        """Save the current line number to checkpoint file"""
        try:
            with open(self.checkpoint_file, 'w') as f:
                json.dump({'last_processed_line': line_number}, f)
        except Exception as e:
            print(f"Error saving checkpoint: {e}")
    
    def get_last_line(self):
        """Get the last processed line number"""
        return self.last_processed_line

def extract_type_from_text(text):
    """Extract the type from the workout data text"""
    match = re.search(r'Type:\s*(\w+)', text)
    if match:
        return match.group(1)
    return "unknown"

def wait_for_rate_limit():
    """Ensure we don't exceed rate limits"""
    now = datetime.now()
    
    # Remove old requests from window
    while REQUESTS_WINDOW and (now - REQUESTS_WINDOW[0]).total_seconds() > 60:
        REQUESTS_WINDOW.popleft()
    
    # If window is full, wait until we can make another request
    if len(REQUESTS_WINDOW) >= RPM_LIMIT:
        wait_time = 60 - (now - REQUESTS_WINDOW[0]).total_seconds()
        if wait_time > 0:
            time.sleep(wait_time)
    
    # Add current request to window
    REQUESTS_WINDOW.append(now)

def clean_entry(entry):
    """Clean a single entry using Groq API"""
    # Extract the text field which contains the workout data and response
    text = entry.get("text", "")
    if not text:
        print("Missing text field")
        return entry

    # Extract type from text
    entry_type = extract_type_from_text(text)
    if entry_type not in ["exercise", "session"]:
        print(f"Unknown entry type: {entry_type}")
        return entry

    # Split into workout data and reasoning/recommendation
    parts = text.split("\n\n\n")
    if len(parts) != 2:
        print("Unexpected text format")
        return entry

    workout_data, analysis = parts

    prompt = f"""Clean and improve this fitness recommendation while maintaining the exact same format. Focus on:
1. Remove any Chinese characters
2. Fix cut-off recommendations
3. Remove thinking process artifacts (like "think Reasoning:", "Template:")
4. Make recommendations and reasoning fitness-focused and evidence-based
5. Ensure recommendations are safe and appropriate
6. Use proper fitness terminology

For {entry_type} entries, keep this exact structure:
{workout_data}

The reasoning and recommendation should be clear and concise, focusing on:
- Evidence-based fitness principles
- Safe and effective exercise modifications
- Clear progression paths
- Practical implementation advice

Original analysis to clean:
{analysis}

Return the complete entry maintaining the exact format with:
1. The 'Workout Data:' section unchanged
2. A 'Reasoning:' section explaining the analysis
3. A 'Recommendation:' section with specific, actionable advice

Make sure to include both 'Reasoning:' and 'Recommendation:' headers in your response."""

    try:
        # Check rate limits before making request
        wait_for_rate_limit()
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are a fitness expert that improves workout recommendations. For {entry_type} entries, keep the exact same format and structure. 
                    Your response must include:
                    1. The original Workout Data section unchanged
                    2. A Reasoning section with the header "Reasoning:"
                    3. A Recommendation section with the header "Recommendation:"
                    Only clean up the reasoning and recommendation content."""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,
            max_tokens=1000
        )
        
        cleaned_text = completion.choices[0].message.content.strip()
        
        # Verify the cleaned text maintains the correct structure
        if not cleaned_text.startswith("Workout Data:"):
            print("Error: Cleaned text does not maintain correct format")
            return entry
            
        if "Reasoning:" not in cleaned_text:
            print("Error: Cleaned text missing Reasoning section")
            return entry
            
        if "Recommendation:" not in cleaned_text:
            print("Error: Cleaned text missing Recommendation section")
            return entry
            
        # Preserve all original fields but update the text
        cleaned_entry = entry.copy()
        cleaned_entry["text"] = cleaned_text
        
        return cleaned_entry
    except Exception as e:
        print(f"Error cleaning entry: {str(e)}")
        return entry

def process_batch(entries, output_file, stats):
    """Process a batch of entries"""
    results = []
    for entry in entries:
        cleaned_entry = clean_entry(entry)
        if cleaned_entry == entry:
            stats["failure"] += 1
        else:
            stats["success"] += 1
        results.append(cleaned_entry)
    
    # Write batch results to file
    with open(output_file, 'a') as outfile:
        for result in results:
            outfile.write(json.dumps(result) + '\n')

def main():
    input_file = "fitness_workout_dataset.jsonl"
    output_file = "fitness_workout_dataset_cleaned.jsonl"
    checkpoint_file = "cleaning_checkpoint.json"
    batch_size = 10  # Process 10 entries at a time
    
    # Initialize checkpoint manager
    checkpoint_mgr = CheckpointManager(checkpoint_file)
    start_line = checkpoint_mgr.get_last_line()
    
    # Count total lines for progress bar
    with open(input_file, 'r') as f:
        total_lines = sum(1 for _ in f)
    
    remaining_lines = total_lines - start_line
    print(f"Processing {remaining_lines} remaining entries starting from line {start_line}...")
    
    # Keep track of success/failure stats
    stats = {"success": 0, "failure": 0}
    
    # Clear or create output file if starting from beginning
    if start_line == 0:
        open(output_file, 'w').close()
    
    # Process entries in batches
    current_batch = []
    current_line = 0
    
    with open(input_file, 'r') as infile:
        with tqdm(total=remaining_lines) as pbar:
            # Skip already processed lines
            for _ in range(start_line):
                next(infile)
                current_line += 1
            
            # Process remaining lines
            for line in infile:
                try:
                    entry = json.loads(line.strip())
                    current_batch.append(entry)
                    current_line += 1
                    
                    if len(current_batch) >= batch_size:
                        process_batch(current_batch, output_file, stats)
                        checkpoint_mgr.save_checkpoint(current_line)
                        pbar.update(len(current_batch))
                        current_batch = []
                except Exception as e:
                    print(f"Error processing line {current_line}: {e}")
                    stats["failure"] += 1
                    pbar.update(1)
                    continue
            
            # Process remaining entries
            if current_batch:
                process_batch(current_batch, output_file, stats)
                checkpoint_mgr.save_checkpoint(current_line)
                pbar.update(len(current_batch))
    
    print("\nProcessing complete!")
    print(f"Successfully cleaned: {stats['success']} entries")
    print(f"Failed to clean: {stats['failure']} entries")
    
    # Clear checkpoint file upon successful completion
    if os.path.exists(checkpoint_file):
        os.remove(checkpoint_file)

if __name__ == "__main__":
    main() 