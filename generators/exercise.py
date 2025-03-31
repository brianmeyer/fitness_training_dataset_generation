"""
Functions for generating exercise examples.
"""

import random
from typing import Dict, Any, List, Optional
from data.feedback import FEEDBACK_TEMPLATES, GOALS
from data.exercises import EXERCISES
from data.muscles import MUSCLE_MAPPINGS
from utils.api import generate_response, validate_response
from .prompts import create_prompt

def get_weighted_exercise() -> tuple[str, str]:
    """Get an exercise using weighted random selection to ensure even distribution."""
    # Weight categories evenly for balanced training data
    category_weights = {
        "compound_barbell": 0.14,    # Equal distribution across categories
        "compound_dumbbell": 0.14,
        "isolation": 0.14,
        "bodyweight": 0.14,
        "machine": 0.14,
        "kettlebell": 0.14,
        "olympic": 0.14
    }
    
    # Select category based on weights
    category = random.choices(
        list(category_weights.keys()),
        weights=list(category_weights.values()),
        k=1
    )[0]
    
    # Get exercise from category
    exercise = random.choice(EXERCISES[category]["exercises"])
    
    return category, exercise

def get_weighted_feedback() -> str:
    """Get feedback using weighted random selection to ensure even distribution."""
    # Weight categories evenly for balanced training data
    category_weights = {
        "positive": 0.33,  # Equal distribution across feedback types
        "neutral": 0.33,
        "negative": 0.34   # Slightly higher to account for rounding
    }
    
    # Select category based on weights
    category = random.choices(
        list(category_weights.keys()),
        weights=list(category_weights.values()),
        k=1
    )[0]
    
    # Select template from category
    return random.choice(FEEDBACK_TEMPLATES[category])

def generate_exercise_example() -> Dict:
    """Generate a single exercise example."""
    # Get weighted exercise
    category, exercise = get_weighted_exercise()
    
    # Get exercise data
    exercise_data = EXERCISES[category]
    weight_range = exercise_data["weight_range"]
    
    # Randomly select weight, reps, sets, and RPE with natural distribution
    weight = random.randint(weight_range[0], weight_range[1])
    reps = random.randint(exercise_data["rep_range"][0], exercise_data["rep_range"][1])
    sets = random.randint(exercise_data["set_range"][0], exercise_data["set_range"][1])
    rpe = random.randint(exercise_data["rpe_range"][0], exercise_data["rpe_range"][1])
    
    # Get weighted feedback
    feedback = get_weighted_feedback()
    
    # Get muscle mappings
    muscle_data = MUSCLE_MAPPINGS[exercise]
    
    return {
        "type": "exercise",  # Set type to "exercise"
        "exercise": exercise,
        "category": category,  # Store the category separately
        "weight": weight,
        "reps": reps,
        "sets": sets,
        "rpe": rpe,
        "feedback": feedback,
        "primary_muscles": muscle_data["primary_muscles"],
        "secondary_muscles": muscle_data["secondary_muscles"],
        "equipment": exercise_data.get("equipment", []),
        "goal": random.choice(GOALS)
    }

def process_exercise_example(example: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Process a single exercise example."""
    try:
        if not validate_muscle_mappings(example):
            print(f"Invalid muscle mappings for exercise: {example.get('exercise', 'unknown')}")
            return None
            
        # Format the workout data
        formatted_workout = (
            f"Workout Data:\n"
            f"- Type: {example['type']}\n"
            f"- Exercise: {example['exercise']}\n"
            f"- Weight: {example['weight']} lbs\n"
            f"- Reps: {example['reps']}\n"
            f"- Sets: {example['sets']}\n"
            f"- RPE: {example['rpe']}\n"
            f"- Primary Muscles: {', '.join(example['primary_muscles'])}\n"
            f"- Secondary Muscles: {', '.join(example['secondary_muscles'])}\n"
            f"- Feedback: {example['feedback']}\n"
            f"- Goal: {example['goal']}\n"
        )
        
        # Create prompt and get API response
        prompt = create_prompt(example, example['goal'])
        response = generate_response(example, prompt)
        if not response:
            print(f"Failed to generate response for exercise: {example.get('exercise', 'unknown')}")
            return None
            
        # Format the final text
        text = f"{formatted_workout}\n\n{response}"
        return {"text": text}
        
    except KeyError as e:
        print(f"Missing required field '{e}' for exercise: {example.get('exercise', 'unknown')}")
        return None
    except Exception as e:
        print(f"Error processing exercise {example.get('exercise', 'unknown')}: {str(e)}")
        return None

def validate_muscle_mappings(example: Dict[str, Any]) -> bool:
    """Validate that the muscle mappings for an exercise are correct."""
    if not example.get('primary_muscles') or not example.get('secondary_muscles'):
        print(f"Missing muscle mappings for {example.get('exercise', 'unknown')}")
        return False
        
    # Check that we have at least one primary muscle
    if len(example['primary_muscles']) == 0:
        print(f"No primary muscles for {example.get('exercise', 'unknown')}")
        return False
        
    return True

def generate_examples(num_examples: int) -> List[Dict[str, Any]]:
    """Generate a batch of exercise examples."""
    examples = []
    max_attempts = num_examples * 2  # Allow up to double the attempts to get valid examples
    attempts = 0
    
    while len(examples) < num_examples and attempts < max_attempts:
        example = generate_exercise_example()
        if example is not None:
            examples.append(example)
        attempts += 1
    
    return examples 