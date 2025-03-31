"""
API interaction functions for generating workout responses.
"""

import re
import os
import requests
from typing import Dict, Any, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .rate_limiter import rate_limiter

# API configuration
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")

API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "qwen-qwq-32b"  # Using the model that worked in trainingdata

# Configure retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

def generate_response(example: Dict[str, Any], prompt: str) -> Optional[str]:
    """Generate a response using the Groq API."""
    try:
        # Wait for rate limits before making request
        rate_limiter.wait_for_rpm()
        rate_limiter.wait_for_rpd()
        
        # Estimate tokens (rough estimate)
        estimated_tokens = len(str(example)) // 4
        rate_limiter.wait_for_tpm(estimated_tokens)
        
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Determine max tokens based on example type
        max_tokens = 2000 if example.get('type') == 'session' else 1000
        
        data = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": """You are a fitness training assistant. Analyze the workout and provide feedback in exactly two sections:

1. Reasoning: Brief analysis of the workout's effectiveness, form, and alignment with the stated goal. For sessions, consider exercise selection, order, and overall volume.

2. Recommendation: Specific, actionable advice for improvement. For sessions, focus on workout structure, exercise modifications, and progression strategies.

IMPORTANT: 
- Your response MUST include "Reasoning:" and "Recommendation:" sections
- Use plain text only - no markdown, no asterisks, no bold, no bullet points
- Keep responses concise and focused on the workout's goal
- Use simple line breaks between points in recommendations"""},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": max_tokens
        }
        
        # Add timeout to the request
        response = session.post(API_ENDPOINT, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        api_response = result['choices'][0]['message']['content'].strip()
        
        # Clean up any markdown formatting
        api_response = re.sub(r'\*\*|\*|__|\[|\]|\(|\)|#|>|`', '', api_response)
        api_response = re.sub(r'\s+', ' ', api_response)  # Normalize whitespace
        api_response = api_response.strip()
        
        # Extract reasoning and recommendation using regex for more robust matching
        # First try exact matches
        reason_match = re.search(r"Reasoning:\s*(.*?)(?=Recommendation:|$)", api_response, re.DOTALL)
        adjust_match = re.search(r"Recommendation:\s*(.*?)$", api_response, re.DOTALL)
        
        # If no exact matches, try case-insensitive
        if not reason_match or not adjust_match:
            reason_match = re.search(r"reasoning:\s*(.*?)(?=recommendation:|$)", api_response, re.DOTALL | re.IGNORECASE)
            adjust_match = re.search(r"recommendation:\s*(.*?)$", api_response, re.DOTALL | re.IGNORECASE)
        
        if not reason_match or not adjust_match:
            print(f"Invalid response format for {example.get('type', 'unknown')} - missing Reasoning: or Recommendation: sections")
            print(f"Response was: {api_response[:100]}...")  # Print first 100 chars of response for debugging
            return None
            
        reasoning = reason_match.group(1).strip()
        recommendation = adjust_match.group(1).strip()
        
        if not reasoning or not recommendation:
            print(f"Invalid response format for {example.get('type', 'unknown')} - empty sections")
            return None
        
        # Format the response in the expected format with consistent spacing
        formatted_response = f"Reasoning: {reasoning}\n\nRecommendation: {recommendation}"
        return formatted_response
        
    except requests.Timeout:
        print(f"API request timed out for {example.get('type', 'unknown')}")
        return None
    except requests.RequestException as e:
        print(f"API request failed for {example.get('type', 'unknown')}: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error for {example.get('type', 'unknown')}: {str(e)}")
        return None

def validate_response(response: str) -> bool:
    """Validate that the response follows the required format and contains appropriate content."""
    if not response:
        return False
    
    # Check for both Reasoning and Recommendation sections
    has_reason = "Reasoning:" in response or "reasoning:" in response.lower()
    has_adjust = "Recommendation:" in response or "recommendation:" in response.lower()
    
    if not (has_reason and has_adjust):
        print("Missing Reasoning: or Recommendation: sections")
        return False
    
    # Extract and validate content
    try:
        # Split response into sections
        sections = response.split("Reasoning:") if "Reasoning:" in response else response.split("reasoning:")
        if len(sections) != 2:
            print("Invalid response format - multiple Reasoning: sections")
            return False
            
        reason_content = sections[1].split("Recommendation:")[0].strip() if "Recommendation:" in sections[1] else sections[1].split("recommendation:")[0].strip()
        adjust_content = sections[1].split("Recommendation:")[1].strip() if "Recommendation:" in sections[1] else sections[1].split("recommendation:")[1].strip()
        
        # Check content quality
        reason_keywords = [
            "rpe", "sets", "reps", "weight", "volume", "intensity", "fatigue", 
            "rest", "order", "session", "effort", "load", "exercise", "form", 
            "technique", "recovery", "goal", "progress"
        ]
        adjust_keywords = [
            "rpe", "sets", "reps", "weight", "lbs", "minutes", "rest", "order", 
            "standardize", "increase", "reduce", "adjust", "form", "technique"
        ]
        
        has_reason_content = any(word in reason_content.lower() for word in reason_keywords)
        has_adjust_content = any(word in adjust_content.lower() for word in adjust_keywords)
        
        # Check content length and quality
        has_content = (
            len(reason_content) > 10 and 
            len(adjust_content) > 10 and
            has_reason_content and
            has_adjust_content
        )
        
        if not has_content:
            print("Content quality check failed")
            return False
            
        return True
        
    except Exception as e:
        print(f"Error parsing response: {e}")
        return False 