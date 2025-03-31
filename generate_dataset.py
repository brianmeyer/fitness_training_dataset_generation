"""
Main script for generating the workout dataset.
"""

import json
import os
from typing import Dict, Any, List
from tqdm import tqdm
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from generators.exercise import generate_examples as generate_exercise_examples, process_exercise_example
from generators.session import generate_examples as generate_session_examples, process_session_example

# Constants
NUM_EXERCISE_EXAMPLES = 3000  # Total exercise examples to generate
NUM_SESSION_EXAMPLES = 2000   # Total session examples to generate
BATCH_SIZE = 100             # Process 100 examples at a time
CHECKPOINT_FILE = "checkpoint.json"
OUTPUT_FILE = "fitness_workout_dataset.jsonl"
MAX_WORKERS = mp.cpu_count()  # Use all available CPU cores

def load_checkpoint() -> Dict[str, int]:
    """Load progress from checkpoint file."""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return json.load(f)
    return {
        "exercise_examples": 0,
        "session_examples": 0,
        "current_batch_size": BATCH_SIZE
    }

def save_checkpoint(exercise_count: int, session_count: int, batch_size: int):
    """Save progress to checkpoint file."""
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({
            "exercise_examples": exercise_count,
            "session_examples": session_count,
            "current_batch_size": batch_size
        }, f)

def write_example(example: Dict[str, Any], output_file: str):
    """Write a single example to output file."""
    with open(output_file, "a") as f:
        f.write(json.dumps(example) + "\n")
        f.flush()  # Ensure immediate write

def process_batch_parallel(examples: List[Dict[str, Any]], example_type: str) -> List[Dict[str, Any]]:
    """Process a batch of examples in parallel."""
    processed_examples = []
    
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        if example_type == "exercise":
            futures = [executor.submit(process_exercise_example, example) for example in examples]
        else:
            futures = [executor.submit(process_session_example, example) for example in examples]
            
        for future in futures:
            result = future.result()
            if result:
                processed_examples.append(result)
    
    return processed_examples

def process_examples(num_examples: int, example_type: str, progress_bar: tqdm) -> int:
    """Process and write examples of a given type."""
    count = 0
    
    while count < num_examples:
        try:
            # Generate batch
            if example_type == "exercise":
                examples = generate_exercise_examples(BATCH_SIZE)
            else:
                examples = generate_session_examples(BATCH_SIZE)
            
            if not examples:
                print(f"Warning: No {example_type} examples generated in batch")
                continue
            
            # Process batch in parallel
            processed_examples = process_batch_parallel(examples, example_type)
            
            # Write processed examples
            for example in processed_examples:
                if example:
                    write_example(example, OUTPUT_FILE)
                    count += 1
                    progress_bar.update(1)
                    
        except Exception as e:
            print(f"Error processing {example_type} batch: {e}")
    
    return count

def main():
    """Main function to generate the dataset."""
    # Load checkpoint
    checkpoint = load_checkpoint()
    exercise_count = checkpoint["exercise_examples"]
    session_count = checkpoint["session_examples"]
    current_batch_size = checkpoint["current_batch_size"]
    
    print("\nDataset generation started. Resuming from checkpoint:")
    print(f"- {exercise_count} exercise examples completed")
    print(f"- {session_count} session examples completed")
    print(f"- Current batch size: {current_batch_size}")
    print(f"- Using {MAX_WORKERS} parallel workers")
    
    # Setup progress bar
    total_examples = NUM_EXERCISE_EXAMPLES + NUM_SESSION_EXAMPLES
    progress_bar = tqdm(total=total_examples, desc="Overall Progress")
    progress_bar.update(exercise_count + session_count)
    
    try:
        while exercise_count < NUM_EXERCISE_EXAMPLES or session_count < NUM_SESSION_EXAMPLES:
            # Alternate between exercise and session examples
            if exercise_count < NUM_EXERCISE_EXAMPLES:
                print("\nProcessing exercise batch...")
                exercise_count += process_examples(
                    min(BATCH_SIZE, NUM_EXERCISE_EXAMPLES - exercise_count),
                    "exercise",
                    progress_bar
                )
                save_checkpoint(exercise_count, session_count, current_batch_size)
            
            if session_count < NUM_SESSION_EXAMPLES:
                print("\nProcessing session batch...")
                session_count += process_examples(
                    min(BATCH_SIZE, NUM_SESSION_EXAMPLES - session_count),
                    "session",
                    progress_bar
                )
                save_checkpoint(exercise_count, session_count, current_batch_size)
    
    except KeyboardInterrupt:
        print("\nInterrupted by user. Saving checkpoint...")
        save_checkpoint(exercise_count, session_count, current_batch_size)
        progress_bar.close()
        return
    
    progress_bar.close()
    print("\nDataset generation completed!")

if __name__ == "__main__":
    main() 