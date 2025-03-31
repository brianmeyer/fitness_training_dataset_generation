"""
Functions for creating prompts for the API.
"""

from typing import Dict, Any
from data.feedback import FEEDBACK_TEMPLATES

def create_prompt(example: Dict[str, Any], goal: str) -> str:
    """Create a prompt for the Groq API using feedback templates."""
    # Create a system prompt that guides the model to use our feedback templates
    system_prompt = """Analyze this workout and provide feedback using the templates below. Keep responses concise and focused.

Current workout:
{workout_data}
Goal: {goal}

Available templates:
{feedback_templates}

Format your response with:
1. Reasoning: Brief analysis of the workout
2. Recommendation: Specific, actionable advice"""
    
    # Format the feedback templates for inclusion in the prompt
    feedback_templates = "Positive:\n"
    for template in FEEDBACK_TEMPLATES["positive"][:3]:  # Include first 3 positive templates
        feedback_templates += f"- {template}\n"
    
    feedback_templates += "\nNeutral:\n"
    for template in FEEDBACK_TEMPLATES["neutral"][:3]:  # Include first 3 neutral templates
        feedback_templates += f"- {template}\n"
    
    feedback_templates += "\nNegative:\n"
    for template in FEEDBACK_TEMPLATES["negative"][:3]:  # Include first 3 negative templates
        feedback_templates += f"- {template}\n"
    
    # Format workout data based on type
    if example['type'] == 'exercise':
        workout_data = (
            f"Type: {example['category']}\n"
            f"Exercise: {example['exercise']}\n"
            f"Weight: {example['weight']} lbs\n"
            f"Sets: {example['sets']}\n"
            f"Reps: {example['reps']}\n"
            f"RPE: {example['rpe']}/10\n"
            f"Primary Muscles: {', '.join(example['primary_muscles'])}\n"
            f"Secondary Muscles: {', '.join(example['secondary_muscles'])}\n"
            f"Equipment: {', '.join(example['equipment'])}\n"
            f"Feedback: {example['feedback']}"
        )
    else:  # session
        workout_data = (
            f"Type: {example['type']}\n"
            f"Duration: {example['duration_minutes']} minutes\n"
            f"Exercises:\n"
        )
        for i, exercise in enumerate(example['exercises'], 1):
            workout_data += (
                f"  {i}. {exercise['exercise']}\n"
                f"     Type: {exercise['type']}\n"
                f"     Weight: {exercise['weight']} lbs\n"
                f"     Sets: {exercise['sets']}\n"
                f"     Reps: {exercise['reps']}\n"
                f"     RPE: {exercise['rpe']}/10\n"
                f"     Primary Muscles: {', '.join(exercise['primary_muscles'])}\n"
                f"     Secondary Muscles: {', '.join(exercise['secondary_muscles'])}\n"
                f"     Equipment: {', '.join(exercise['equipment'])}\n"
            )
        workout_data += f"Feedback: {example['feedback']}"
    
    # Format the prompt with the workout data and feedback templates
    return system_prompt.format(
        workout_data=workout_data,
        goal=goal,
        feedback_templates=feedback_templates
    ) 