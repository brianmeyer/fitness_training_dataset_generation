"""
Quality control functions for dataset generation.
"""

import random
from typing import Dict, List, Any

def quality_check(examples: List[Dict[str, Any]], batch_type: str) -> bool:
    """Perform quality check on random sample of examples."""
    if not examples:
        return False
        
    print(f"\nPerforming quality check on {batch_type} examples...")
    sample_size = min(25, len(examples))
    samples = random.sample(examples, sample_size)
    
    print(f"\nAnalyzing {sample_size} random samples:")
    valid_count = 0
    issues = []
    
    for i, example in enumerate(samples, 1):
        print(f"\nSample {i}:")
        text = example.get('text', '')
        
        # Check for required sections
        required_sections = ['Workout Data:', 'Reasoning:', 'Recommendation:']
        if not all(section in text for section in required_sections):
            issues.append(f"Missing required sections in sample {i}")
            continue
            
        # Check content quality
        sections = text.split('\n\n')
        if len(sections) < 3:
            issues.append(f"Invalid format in sample {i}")
            continue
            
        valid_count += 1
    
    print(f"\nQuality Check Results:")
    print(f"Valid samples: {valid_count}/{sample_size}")
    if issues:
        print("\nIssues found:")
        for issue in issues:
            print(f"- {issue}")
    
    # Require at least 90% valid samples
    return valid_count / sample_size >= 0.9

def check_batch_quality(examples: List[Dict[str, Any]], example_type: str) -> bool:
    """Check the quality of processed examples."""
    if not examples:
        return False
        
    # Basic quality checks
    for example in examples:
        if not example or "text" not in example:
            return False
            
        # Check for minimum content length
        if len(example["text"]) < 100:  # Arbitrary minimum length
            return False
            
        # Check for required sections in the text
        text = example["text"].lower()
        if "reasoning:" not in text or "recommendation:" not in text:
            return False
            
    return True 