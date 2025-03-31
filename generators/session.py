"""
Functions for generating session examples.
"""

import random
from typing import Dict, Any, List, Optional, Set
from data.feedback import FEEDBACK_TEMPLATES, GOALS
from data.exercises import EXERCISES
from data.muscles import MUSCLE_MAPPINGS
from utils.api import generate_response, validate_response
from .prompts import create_prompt

# Track used exercises and feedback to ensure variety
used_exercises: Set[str] = set()
used_feedback: Dict[str, Set[str]] = {
    "positive": set(),
    "neutral": set(),
    "negative": set()
}

def reset_tracking():
    """Reset the tracking of used exercises and feedback."""
    global used_exercises, used_feedback
    used_exercises.clear()
    for category in used_feedback:
        used_feedback[category].clear()

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
    
    # Get available exercises from category that haven't been used recently
    available_exercises = [ex for ex in EXERCISES[category]["exercises"] if ex not in used_exercises]
    
    # If all exercises have been used, reset the tracking
    if not available_exercises:
        used_exercises.clear()
        available_exercises = EXERCISES[category]["exercises"]
    
    # Select exercise from available ones
    exercise = random.choice(available_exercises)
    used_exercises.add(exercise)
    
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
    
    # Get available templates that haven't been used recently
    available_templates = [t for t in FEEDBACK_TEMPLATES[category] if t not in used_feedback[category]]
    
    # If all templates have been used, reset the tracking for this category
    if not available_templates:
        used_feedback[category].clear()
        available_templates = FEEDBACK_TEMPLATES[category]
    
    # Select template from available ones
    template = random.choice(available_templates)
    used_feedback[category].add(template)
    
    return template

def generate_session_example() -> Dict:
    """Generate a complete training session example."""
    # Evenly distribute session complexity (6-10 exercises)
    num_exercises = random.randint(6, 10)
    exercises = []
    
    # Generate exercises for the session
    for _ in range(num_exercises):
        # Get weighted exercise
        category, exercise = get_weighted_exercise()
        
        # Get exercise data
        exercise_data = EXERCISES[category]
        weight_range = exercise_data["weight_range"]
        
        # Randomly select weight, reps, sets, and RPE with even distribution
        weight = random.randint(weight_range[0], weight_range[1])
        reps = random.randint(exercise_data["rep_range"][0], exercise_data["rep_range"][1])
        sets = random.randint(exercise_data["set_range"][0], exercise_data["set_range"][1])
        rpe = random.randint(exercise_data["rpe_range"][0], exercise_data["rpe_range"][1])
        
        # Get muscle mappings
        muscle_data = MUSCLE_MAPPINGS[exercise]
        
        exercises.append({
            "exercise": exercise,
            "type": category,
            "weight": weight,
            "reps": reps,
            "sets": sets,
            "rpe": rpe,
            "primary_muscles": muscle_data["primary_muscles"],
            "secondary_muscles": muscle_data["secondary_muscles"],
            "equipment": exercise_data.get("equipment", [])
        })
    
    # Estimate total duration (2-3 minutes per set)
    total_sets = sum(ex["sets"] for ex in exercises)
    duration_minutes = total_sets * 2.5
    
    # Get weighted feedback
    feedback = get_weighted_feedback()
    
    # Select goal with even distribution
    goal = random.choice(GOALS)
    
    return {
        "type": "session",
        "exercises": exercises,
        "duration_minutes": duration_minutes,
        "feedback": feedback,
        "goal": goal
    }

def process_session_example(example: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Process a single session example."""
    try:
        if not validate_session_exercises(example):
            print(f"Invalid exercises in session")
            return None
            
        # Format the workout data
        formatted_workout = (
            f"Workout Data:\n"
            f"- Type: {example['type']}\n"
            f"- Duration: {example['duration_minutes']} minutes\n"
            f"- Goal: {example['goal']}\n"
            f"- Exercises:\n"
        )
        
        for i, exercise in enumerate(example["exercises"], 1):
            formatted_workout += (
                f"  {i}. {exercise['exercise']}\n"
                f"     - Type: {exercise['type']}\n"
                f"     - Weight: {exercise['weight']} lbs\n"
                f"     - Reps: {exercise['reps']}\n"
                f"     - Sets: {exercise['sets']}\n"
                f"     - RPE: {exercise['rpe']}\n"
                f"     - Primary Muscles: {', '.join(exercise['primary_muscles'])}\n"
                f"     - Secondary Muscles: {', '.join(exercise['secondary_muscles'])}\n"
                f"     - Equipment: {', '.join(exercise['equipment'])}\n"
            )
        
        formatted_workout += f"- Feedback: {example['feedback']}\n"
        
        # Create prompt and get API response
        prompt = create_prompt(example, example['goal'])
        response = generate_response(example, prompt)
        if not response:
            print(f"Failed to generate response for session")
            return None
            
        # Format the final text
        text = f"{formatted_workout}\n\n{response}"
        return {"text": text}
        
    except KeyError as e:
        print(f"Missing required field '{e}' in session example")
        return None
    except Exception as e:
        print(f"Error processing session: {str(e)}")
        return None

def validate_session_exercises(example: Dict[str, Any]) -> bool:
    """Validate that all exercises in a session have correct muscle mappings."""
    if not example.get('exercises'):
        print("No exercises in session")
        return False
        
    for i, exercise in enumerate(example['exercises'], 1):
        if not exercise.get('primary_muscles') or not exercise.get('secondary_muscles'):
            print(f"Missing muscle mappings for exercise {i}: {exercise.get('exercise', 'unknown')}")
            return False
            
        # Check that we have at least one primary muscle
        if len(exercise['primary_muscles']) == 0:
            print(f"No primary muscles for exercise {i}: {exercise.get('exercise', 'unknown')}")
            return False
            
    return True

def generate_examples(num_examples: int) -> List[Dict[str, Any]]:
    """Generate a batch of session examples."""
    examples = []
    max_attempts = num_examples * 2  # Allow up to double the attempts to get valid examples
    attempts = 0
    
    while len(examples) < num_examples and attempts < max_attempts:
        example = generate_session_example()
        if example is not None:
            examples.append(example)
        attempts += 1
    
    return examples 