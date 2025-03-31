"""
Checkpoint management functions for dataset generation.
"""

import json
import os
from typing import Dict

# Constants
CHECKPOINT_FILE = "checkpoint.json"
BATCH_SIZES = {
    'exercise': [500] * 6,  # 6 batches of 500 for exercises
    'session': [500] * 4    # 4 batches of 500 for sessions
}

def load_checkpoint() -> Dict[str, int]:
    """Load checkpoint from file if it exists."""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r') as f:
            checkpoint = json.load(f)
            print(f"Resuming from checkpoint:")
            print(f"Exercise examples: {checkpoint['exercise_count']}")
            print(f"Session examples: {checkpoint['session_count']}")
            print(f"Current batch size: {checkpoint['current_batch_size']}")
            return checkpoint
    return {
        'exercise_count': 0,
        'session_count': 0,
        'current_batch_size': BATCH_SIZES['exercise'][0]
    }

def save_checkpoint(exercise_count: int, session_count: int, batch_size: int):
    """Save current progress to checkpoint file."""
    checkpoint = {
        'exercise_count': exercise_count,
        'session_count': session_count,
        'current_batch_size': batch_size,
    }
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f)

def get_next_batch_size(batch_type: str) -> int:
    """Get the next batch size based on current progress."""
    sizes = BATCH_SIZES[batch_type]
    current_size = 0
    for size in sizes:
        if size > current_size:
            return size
    return sizes[-1] 