"""
Muscle mappings for exercises.
"""

# Muscle mappings for different exercises
MUSCLE_MAPPINGS = {
    # Compound Barbell Exercises
    "Bench Press": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Overhead Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Incline Bench Press": {
        "primary_muscles": ["upper chest (clavicular head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Decline Bench Press": {
        "primary_muscles": ["lower chest (sternal head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Close Grip Bench Press": {
        "primary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Behind the Neck Press": {
        "primary_muscles": ["shoulders (deltoids)", "triceps (triceps brachii)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Floor Press": {
        "primary_muscles": ["chest (pectoralis major)", "triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Back Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Front Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Box Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Pause Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Safety Squat Bar Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Zercher Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)", "biceps (biceps brachii)"]
    },
    "Overhead Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Split Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Bulgarian Split Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Conventional Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Sumo Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Romanian Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Deficit Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Block Pull": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Rack Pull": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Snatch Grip Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Trap Bar Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Barbell Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Pendlay Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Meadows Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "T-Bar Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Seal Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Bent Over Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Yates Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Power Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Power Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Power Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Good Morning": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Landmine Press": {
        "primary_muscles": ["shoulders (deltoids)", "chest (pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Landmine Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Landmine Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Zercher Carry": {
        "primary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)", "traps (trapezius)", "forearms"]
    },
    "Farmer's Carry": {
        "primary_muscles": ["forearms", "traps (trapezius)"],
        "secondary_muscles": ["core (rectus abdominis)", "quadriceps (vastus muscles)"]
    },
    # Compound Dumbbell Exercises
    "Dumbbell Press": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Incline Dumbbell Press": {
        "primary_muscles": ["upper chest (clavicular head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Decline Dumbbell Press": {
        "primary_muscles": ["lower chest (sternal head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Dumbbell Shoulder Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Arnold Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Seated Dumbbell Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Dumbbell Push Press": {
        "primary_muscles": ["shoulders (deltoids)", "quadriceps (vastus muscles)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)", "glutes (gluteus maximus)"]
    },
    "Dumbbell Push Jerk": {
        "primary_muscles": ["shoulders (deltoids)", "quadriceps (vastus muscles)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)", "glutes (gluteus maximus)"]
    },
    "Goblet Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Dumbbell Front Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Dumbbell Walking Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Dumbbell Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Dumbbell Box Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Dumbbell Split Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Dumbbell Romanian Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Dumbbell Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Dumbbell Renegade Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Dumbbell Meadows Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Dumbbell Single Arm Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Dumbbell High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Dumbbell Upright Row": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["biceps (biceps brachii)"]
    },
    "Dumbbell Stiff Leg Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Dumbbell Sumo Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)"]
    },
    "Dumbbell Deficit Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)"]
    },
    "Dumbbell Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Dumbbell Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Dumbbell Thruster": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Dumbbell Swing": {
        "primary_muscles": ["hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Dumbbell Turkish Get-up": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)", "triceps (triceps brachii)"]
    },
    "Dumbbell Windmill": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["hamstrings", "glutes (gluteus maximus)"]
    },
    "Dumbbell Figure 8": {
        "primary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)", "forearms"]
    },
    "Dumbbell Halo": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Dumbbell Carry": {
        "primary_muscles": ["forearms", "traps (trapezius)"],
        "secondary_muscles": ["core (rectus abdominis)", "quadriceps (vastus muscles)"]
    },
    # Isolation Exercises
    "Dumbbell Fly": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Cable Fly": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Pec Deck": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Chest Fly": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Incline Fly": {
        "primary_muscles": ["upper chest (clavicular head of pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Decline Fly": {
        "primary_muscles": ["lower chest (sternal head of pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Cable Crossover": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Machine Fly": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    
    # Shoulders
    "Lateral Raise": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)"]
    },
    "Front Raise": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)"]
    },
    "Reverse Fly": {
        "primary_muscles": ["rear deltoids"],
        "secondary_muscles": ["traps (trapezius)", "rhomboids"]
    },
    "Face Pull": {
        "primary_muscles": ["rear deltoids", "traps (trapezius)"],
        "secondary_muscles": ["rhomboids", "rotator cuff"]
    },
    "Cable Lateral Raise": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)"]
    },
    "Machine Lateral Raise": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)"]
    },
    "Dumbbell Shrug": {
        "primary_muscles": ["traps (trapezius)"],
        "secondary_muscles": ["levator scapulae"]
    },
    "Cable Shrug": {
        "primary_muscles": ["traps (trapezius)"],
        "secondary_muscles": ["levator scapulae"]
    },
    "Machine Shrug": {
        "primary_muscles": ["traps (trapezius)"],
        "secondary_muscles": ["levator scapulae"]
    },
    
    # Back
    "Straight Arm Pulldown": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["chest (pectoralis major)", "core (rectus abdominis)"]
    },
    "Cable Pullover": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["chest (pectoralis major)", "triceps (triceps brachii)"]
    },
    "Machine Pullover": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["chest (pectoralis major)", "triceps (triceps brachii)"]
    },
    "Reverse Grip Pulldown": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "traps (trapezius)"]
    },
    "Close Grip Pulldown": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "traps (trapezius)"]
    },
    "Wide Grip Pulldown": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "traps (trapezius)"]
    },
    
    # Biceps
    "Bicep Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Hammer Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Preacher Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Concentration Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Incline Dumbbell Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Spider Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Cable Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Machine Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    "Reverse Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (extensor carpi radialis)"]
    },
    "Zottman Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)", "forearms (extensor carpi radialis)"]
    },
    "Cross Body Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms (flexor carpi radialis)"]
    },
    
    # Triceps
    "Tricep Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Skull Crusher": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Overhead Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Cable Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Machine Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Rope Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Close Grip Push-up": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["chest (pectoralis major)", "shoulders (deltoids)"]
    },
    "Diamond Push-up": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["chest (pectoralis major)", "shoulders (deltoids)"]
    },
    "Tricep Kickback": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Tricep Pushdown": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Single Arm Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    
    # Legs
    "Leg Extension": {
        "primary_muscles": ["quadriceps (vastus muscles)"],
        "secondary_muscles": ["hip flexors (iliopsoas)", "core (rectus abdominis)"]
    },
    "Leg Curl": {
        "primary_muscles": ["hamstrings"],
        "secondary_muscles": ["calves (gastrocnemius)"]
    },
    "Calf Raise": {
        "primary_muscles": ["calves (gastrocnemius)"],
        "secondary_muscles": ["soleus"]
    },
    "Seated Calf Raise": {
        "primary_muscles": ["soleus"],
        "secondary_muscles": ["calves (gastrocnemius)"]
    },
    "Standing Calf Raise": {
        "primary_muscles": ["calves (gastrocnemius)"],
        "secondary_muscles": ["soleus"]
    },
    "Machine Calf Raise": {
        "primary_muscles": ["calves (gastrocnemius)"],
        "secondary_muscles": ["soleus"]
    },
    "Donkey Calf Raise": {
        "primary_muscles": ["calves (gastrocnemius)"],
        "secondary_muscles": ["soleus"]
    },
    "Hip Abduction": {
        "primary_muscles": ["glutes (gluteus medius)"],
        "secondary_muscles": ["tensor fasciae latae"]
    },
    "Hip Adduction": {
        "primary_muscles": ["adductors"],
        "secondary_muscles": ["gracilis"]
    },
    "Inner Thigh": {
        "primary_muscles": ["adductors"],
        "secondary_muscles": ["gracilis"]
    },
    "Outer Thigh": {
        "primary_muscles": ["glutes (gluteus medius)"],
        "secondary_muscles": ["tensor fasciae latae"]
    },
    "Machine Leg Press": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)"]
    },
    "Machine Hack Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)"]
    },
    "Machine Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)"]
    },
    
    # Core
    "Cable Crunch": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques"]
    },
    "Machine Crunch": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques"]
    },
    "Ab Crunch": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques"]
    },
    "Reverse Crunch": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques"]
    },
    "Hanging Leg Raise": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques", "hip flexors"]
    },
    "Cable Woodchop": {
        "primary_muscles": ["obliques"],
        "secondary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Russian Twist": {
        "primary_muscles": ["obliques"],
        "secondary_muscles": ["core (rectus abdominis)"]
    },
    "Side Plank": {
        "primary_muscles": ["obliques"],
        "secondary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Plank": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)", "back (erector spinae)"]
    },
    "Mountain Climber": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)", "hip flexors"]
    },
    "Flutter Kick": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["hip flexors"]
    },
    "Bicycle Crunch": {
        "primary_muscles": ["core (rectus abdominis)", "obliques"],
        "secondary_muscles": ["hip flexors"]
    },
    
    # Forearms
    "Wrist Curl": {
        "primary_muscles": ["forearms (flexor carpi radialis, flexor carpi ulnaris)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Reverse Wrist Curl": {
        "primary_muscles": ["forearms (extensor carpi radialis, extensor carpi ulnaris)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Wrist Extension": {
        "primary_muscles": ["forearms (extensor carpi radialis, extensor carpi ulnaris)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Wrist Flexion": {
        "primary_muscles": ["forearms (flexor carpi radialis, flexor carpi ulnaris)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Farmer's Carry": {
        "primary_muscles": ["forearms", "traps (trapezius)"],
        "secondary_muscles": ["core (rectus abdominis)", "quadriceps (vastus muscles)"]
    },
    "Plate Pinch": {
        "primary_muscles": ["forearms (flexor digitorum profundus, flexor digitorum superficialis)"],
        "secondary_muscles": ["shoulders (deltoids)", "traps (trapezius)"]
    },
    "Towel Pull-up": {
        "primary_muscles": ["forearms"],
        "secondary_muscles": ["back (latissimus dorsi)", "biceps (biceps brachii)"]
    },
    "Dead Hang": {
        "primary_muscles": ["forearms"],
        "secondary_muscles": ["shoulders (deltoids)", "back (latissimus dorsi)"]
    },
    
    # Glutes
    "Hip Thrust": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    "Glute Kickback": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings"]
    },
    "Machine Hip Thrust": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    "Cable Hip Thrust": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    "Banded Hip Thrust": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    "Glute Bridge": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    "Single Leg Hip Thrust": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    
    # Lower Back
    "Back Extension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Machine Back Extension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Cable Back Extension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Reverse Hyperextension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Machine Reverse Hyper": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    
    # Olympic Lifts
    "Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Clean and Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "triceps (triceps brachii)"]
    },
    "Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Power Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Power Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Split Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Split Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Push Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Push Press": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    
    # Pulling Variations
    "Clean Pull": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)"]
    },
    "Snatch Pull": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)"]
    },
    "High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Clean Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Snatch Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Deficit Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Block Pull": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Rack Pull": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    
    # Hang Variations
    "Hang Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Hang Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "High Hang Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "High Hang Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Low Hang Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Low Hang Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Block Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Block Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    
    # Jerk Variations
    "Split Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Push Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Power Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Behind the Neck Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Behind the Neck Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "traps (trapezius)"]
    },
    
    # Assistance Lifts
    "Clean Grip Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Snatch Grip Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Romanian Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Good Morning": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Back Extension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["hamstrings", "glutes (gluteus maximus)"]
    },
    "Reverse Hyperextension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["hamstrings", "glutes (gluteus maximus)"]
    },
    
    # Technical Drills
    "Clean High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Snatch High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Clean Extension": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Snatch Extension": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Clean Recovery": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Snatch Recovery": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    
    # Complexes
    "Clean + Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)", "triceps (triceps brachii)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Snatch + Overhead Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Clean + Front Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Clean + Push Press": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)", "triceps (triceps brachii)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Clean + Jerk + Front Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)", "triceps (triceps brachii)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "lower back (erector spinae)"]
    },
    "Kettlebell Thruster": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Swing": {
        "primary_muscles": ["hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"]
    },
    
    # Bodyweight Exercises
    "Push-up": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Incline Push-up": {
        "primary_muscles": ["upper chest (clavicular head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Decline Push-up": {
        "primary_muscles": ["lower chest (sternal head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Pike Push-up": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Handstand Push-up": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Dips": {
        "primary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Bench Dips": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["chest (pectoralis major)", "shoulders (deltoids)"]
    },
    "Ring Dips": {
        "primary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Pseudo Planche Push-up": {
        "primary_muscles": ["chest (pectoralis major)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Chin-up": {
        "primary_muscles": ["back (latissimus dorsi)", "biceps (biceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)"]
    },
    "Neutral Grip Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Wide Grip Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Close Grip Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)", "biceps (biceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)"]
    },
    "L-Sit Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)"]
    },
    "Muscle-up": {
        "primary_muscles": ["back (latissimus dorsi)", "chest (pectoralis major)"],
        "secondary_muscles": ["biceps (biceps brachii)", "triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Inverted Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Australian Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Ring Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Bodyweight Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Hollow Hold": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["hip flexors"]
    },
    "Arch Hold": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Superman Hold": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "L-Sit": {
        "primary_muscles": ["core (rectus abdominis)", "triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)", "hip flexors"]
    },
    "Toes to Bar": {
        "primary_muscles": ["core (rectus abdominis)", "hip flexors"],
        "secondary_muscles": ["back (latissimus dorsi)"]
    },
    "Knee to Elbow": {
        "primary_muscles": ["core (rectus abdominis)", "hip flexors"],
        "secondary_muscles": ["obliques"]
    },
    "Bodyweight Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Pistol Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Jump Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Walking Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Reverse Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Box Jump": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Broad Jump": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Burpee": {
        "primary_muscles": ["chest (pectoralis major)", "quadriceps (vastus muscles)"],
        "secondary_muscles": ["shoulders (deltoids)", "triceps (triceps brachii)", "core (rectus abdominis)", "hamstrings"]
    },
    "Bear Crawl": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "quadriceps (vastus muscles)"]
    },
    "Crab Walk": {
        "primary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)", "hamstrings"]
    },
    "Inchworm": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)"]
    },
    "Spider-man Crawl": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "hip flexors"]
    },
    "Animal Flow": {
        "primary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "quadriceps (vastus muscles)", "hamstrings"]
    },
    "Handstand Walk": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Handstand": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Front Lever": {
        "primary_muscles": ["back (latissimus dorsi)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Back Lever": {
        "primary_muscles": ["back (latissimus dorsi)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Planche": {
        "primary_muscles": ["chest (pectoralis major)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Skin the Cat": {
        "primary_muscles": ["back (latissimus dorsi)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    "Human Flag": {
        "primary_muscles": ["back (latissimus dorsi)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)", "shoulders (deltoids)"]
    },
    
    # Kettlebell Exercises
    "Kettlebell Snatch": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Kettlebell Clean": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Kettlebell Clean and Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "triceps (triceps brachii)"]
    },
    "Kettlebell Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Push Press": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Push Jerk": {
        "primary_muscles": ["quadriceps (vastus muscles)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Long Cycle": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)", "core (rectus abdominis)", "triceps (triceps brachii)"]
    },
    "Kettlebell Goblet Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Front Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Rack Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Overhead Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Kettlebell Split Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Bulgarian Split Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Box Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Pistol Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Kettlebell Romanian Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Kettlebell Sumo Deadlift": {
        "primary_muscles": ["lower back (erector spinae)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "core (rectus abdominis)", "traps (trapezius)"]
    },
    "Kettlebell Stiff Leg Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Kettlebell Single Leg Deadlift": {
        "primary_muscles": ["hamstrings", "lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "core (rectus abdominis)"]
    },
    "Kettlebell Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Military Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Arnold Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Kettlebell Renegade Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Kettlebell Single Arm Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Kettlebell Meadows Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids", "core (rectus abdominis)"]
    },
    "Kettlebell High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Kettlebell Upright Row": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["biceps (biceps brachii)"]
    },
    "Kettlebell Turkish Get-up": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)", "triceps (triceps brachii)"]
    },
    "Kettlebell Windmill": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["hamstrings", "glutes (gluteus maximus)"]
    },
    "Kettlebell Figure 8": {
        "primary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)", "forearms"]
    },
    "Kettlebell Halo": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Arm Bar": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Bottoms Up Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)", "forearms"]
    },
    "Kettlebell Walking Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Reverse Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Box Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Cossack Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)", "adductors"]
    },
    "Kettlebell Plank": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)", "back (erector spinae)"]
    },
    "Kettlebell Side Plank": {
        "primary_muscles": ["obliques"],
        "secondary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"]
    },
    "Kettlebell Suitcase Carry": {
        "primary_muscles": ["core (rectus abdominis)", "forearms"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "traps (trapezius)"]
    },
    "Kettlebell Rack Carry": {
        "primary_muscles": ["core (rectus abdominis)", "quadriceps (vastus muscles)"],
        "secondary_muscles": ["shoulders (deltoids)", "traps (trapezius)"]
    },
    "Kettlebell Overhead Carry": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Waiter Carry": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Flow": {
        "primary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Kettlebell Circuit": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell Complex": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell EMOM": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell Tabata": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell AMRAP": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    # Machine Exercises
    "Machine Decline Press": {
        "primary_muscles": ["lower chest (sternal head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Machine Incline Press": {
        "primary_muscles": ["upper chest (clavicular head of pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"]
    },
    "Machine Shoulder Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Machine Military Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Machine Seated Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Machine Dip": {
        "primary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Machine Tricep Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Machine Pec Deck": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Lat Pulldown": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids"]
    },
    "Machine Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids"]
    },
    "Seated Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids"]
    },
    "Cable Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids"]
    },
    "Machine Pullover": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["chest (pectoralis major)", "triceps (triceps brachii)"]
    },
    "Machine High Row": {
        "primary_muscles": ["upper back (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids"]
    },
    "Machine Low Row": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "rear deltoids"]
    },
    "Machine Reverse Fly": {
        "primary_muscles": ["rear deltoids"],
        "secondary_muscles": ["traps (trapezius)", "rhomboids"]
    },
    "Machine Back Extension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Machine Reverse Hyperextension": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Machine Bicep Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms"]
    },
    "Machine Preacher Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms"]
    },
    "Cable Bicep Curl": {
        "primary_muscles": ["biceps (biceps brachii)"],
        "secondary_muscles": ["forearms"]
    },
    "Cable Tricep Extension": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Cable Lateral Raise": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["traps (trapezius)"]
    },
    "Cable Front Raise": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["chest (pectoralis major)"]
    },
    "Cable Face Pull": {
        "primary_muscles": ["rear deltoids", "traps (trapezius)"],
        "secondary_muscles": ["rhomboids"]
    },
    "Cable Shrug": {
        "primary_muscles": ["traps (trapezius)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Leg Press": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)"]
    },
    "Hack Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)"]
    },
    "Smith Machine Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Machine Leg Extension": {
        "primary_muscles": ["quadriceps (vastus muscles)"],
        "secondary_muscles": ["hip flexors"]
    },
    "Machine Leg Curl": {
        "primary_muscles": ["hamstrings"],
        "secondary_muscles": ["calves (gastrocnemius)"]
    },
    "Machine Calf Raise": {
        "primary_muscles": ["calves (gastrocnemius)"],
        "secondary_muscles": ["soleus"]
    },
    "Machine Hip Thrust": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "core (rectus abdominis)"]
    },
    "Machine Hip Abduction": {
        "primary_muscles": ["gluteus medius"],
        "secondary_muscles": ["tensor fasciae latae"]
    },
    "Machine Hip Adduction": {
        "primary_muscles": ["adductors"],
        "secondary_muscles": ["gluteus medius"]
    },
    "Machine Inner Thigh": {
        "primary_muscles": ["adductors"],
        "secondary_muscles": ["gluteus medius"]
    },
    "Machine Outer Thigh": {
        "primary_muscles": ["gluteus medius"],
        "secondary_muscles": ["tensor fasciae latae"]
    },
    "Machine Glute Kickback": {
        "primary_muscles": ["glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings"]
    },
    "Machine Ab Crunch": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques"]
    },
    "Machine Torso Rotation": {
        "primary_muscles": ["obliques"],
        "secondary_muscles": ["core (rectus abdominis)"]
    },
    "Machine Woodchop": {
        "primary_muscles": ["obliques", "core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Cable Crunch": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["obliques"]
    },
    "Cable Woodchop": {
        "primary_muscles": ["obliques", "core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Cable Pull-through": {
        "primary_muscles": ["glutes (gluteus maximus)", "hamstrings"],
        "secondary_muscles": ["core (rectus abdominis)"]
    },
    "Cable Crossover": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Cable Fly": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"]
    },
    "Cable Pullover": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["chest (pectoralis major)", "triceps (triceps brachii)"]
    },
    "Cable Upright Row": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["biceps (biceps brachii)"]
    },
    "Cable Tricep Pushdown": {
        "primary_muscles": ["triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    
    # Bodyweight Exercises
    "Wide Push-up": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Close Grip Push-up": {
        "primary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"],
        "secondary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Chin-up": {
        "primary_muscles": ["back (latissimus dorsi)", "biceps (biceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)"]
    },
    "Neutral Grip Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Wide Grip Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Close Grip Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "L-Sit Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)", "core (rectus abdominis)"],
        "secondary_muscles": ["biceps (biceps brachii)"]
    },
    "Muscle-up": {
        "primary_muscles": ["back (latissimus dorsi)", "chest (pectoralis major)", "triceps (triceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)", "biceps (biceps brachii)"]
    },
    "Inverted Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Australian Pull-up": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Ring Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Bodyweight Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Hollow Hold": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["hip flexors"]
    },
    "Arch Hold": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "Superman Hold": {
        "primary_muscles": ["lower back (erector spinae)"],
        "secondary_muscles": ["glutes (gluteus maximus)", "hamstrings"]
    },
    "L-Sit": {
        "primary_muscles": ["core (rectus abdominis)", "triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)", "hip flexors"]
    },
    "Toes to Bar": {
        "primary_muscles": ["core (rectus abdominis)", "hip flexors"],
        "secondary_muscles": ["back (latissimus dorsi)"]
    },
    "Knee to Elbow": {
        "primary_muscles": ["core (rectus abdominis)", "hip flexors"],
        "secondary_muscles": ["obliques"]
    },
    "Bodyweight Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Pistol Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Jump Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Walking Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Reverse Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Box Jump": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Broad Jump": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Burpee": {
        "primary_muscles": ["chest (pectoralis major)", "quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["shoulders (deltoids)", "triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Mountain Climber": {
        "primary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"],
        "secondary_muscles": ["hip flexors", "triceps (triceps brachii)"]
    },
    "Bear Crawl": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "hip flexors"]
    },
    "Crab Walk": {
        "primary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)"],
        "secondary_muscles": ["core (rectus abdominis)", "hip flexors"]
    },
    "Inchworm": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "hip flexors"]
    },
    "Spider-man Crawl": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "hip flexors"]
    },
    "Animal Flow": {
        "primary_muscles": ["core (rectus abdominis)", "shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "hip flexors"]
    },
    "Handstand Walk": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    
    # Kettlebell Exercises
    "Kettlebell Floor Press": {
        "primary_muscles": ["chest (pectoralis major)", "triceps (triceps brachii)"],
        "secondary_muscles": ["shoulders (deltoids)"]
    },
    "Kettlebell Military Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Kettlebell Arnold Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "chest (pectoralis major)"]
    },
    "Kettlebell Renegade Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Single Arm Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Meadows Row": {
        "primary_muscles": ["back (latissimus dorsi)", "traps (trapezius)"],
        "secondary_muscles": ["biceps (biceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell High Pull": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"]
    },
    "Kettlebell Upright Row": {
        "primary_muscles": ["traps (trapezius)", "shoulders (deltoids)"],
        "secondary_muscles": ["biceps (biceps brachii)"]
    },
    "Kettlebell Turkish Get-up": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "glutes (gluteus maximus)"]
    },
    "Kettlebell Windmill": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["hamstrings", "glutes (gluteus maximus)"]
    },
    "Kettlebell Figure 8": {
        "primary_muscles": ["shoulders (deltoids)", "biceps (biceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)", "forearms"]
    },
    "Kettlebell Halo": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Arm Bar": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Bottoms Up Press": {
        "primary_muscles": ["shoulders (deltoids)"],
        "secondary_muscles": ["triceps (triceps brachii)", "core (rectus abdominis)"]
    },
    "Kettlebell Walking Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Reverse Lunge": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Box Step-up": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Cossack Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "glutes (gluteus maximus)"],
        "secondary_muscles": ["hamstrings", "calves (gastrocnemius)", "core (rectus abdominis)"]
    },
    "Kettlebell Plank": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["shoulders (deltoids)", "triceps (triceps brachii)"]
    },
    "Kettlebell Side Plank": {
        "primary_muscles": ["core (rectus abdominis)", "obliques"],
        "secondary_muscles": ["shoulders (deltoids)", "triceps (triceps brachii)"]
    },
    "Kettlebell Suitcase Carry": {
        "primary_muscles": ["core (rectus abdominis)", "forearms"],
        "secondary_muscles": ["traps (trapezius)", "quadriceps (vastus muscles)"]
    },
    "Kettlebell Rack Carry": {
        "primary_muscles": ["core (rectus abdominis)", "forearms"],
        "secondary_muscles": ["traps (trapezius)", "quadriceps (vastus muscles)"]
    },
    "Kettlebell Overhead Carry": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Waiter Carry": {
        "primary_muscles": ["shoulders (deltoids)", "core (rectus abdominis)"],
        "secondary_muscles": ["triceps (triceps brachii)", "forearms"]
    },
    "Kettlebell Flow": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell Circuit": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell Complex": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell EMOM": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell Tabata": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Kettlebell AMRAP": {
        "primary_muscles": ["core (rectus abdominis)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)", "shoulders (deltoids)"]
    },
    "Behind the Neck Squat": {
        "primary_muscles": ["quadriceps (vastus muscles)", "hamstrings", "glutes (gluteus maximus)"],
        "secondary_muscles": ["core (rectus abdominis)", "lower back (erector spinae)", "shoulders (deltoids)"]
    },
    "Deadlift": {
        "primary_muscles": ["hamstrings", "glutes (gluteus maximus)", "lower back (erector spinae)"],
        "secondary_muscles": ["quadriceps (vastus muscles)", "traps (trapezius)", "core (rectus abdominis)"]
    },
    "Machine Chest Press": {
        "primary_muscles": ["chest (pectoralis major)"],
        "secondary_muscles": ["triceps (triceps brachii)", "shoulders (deltoids)", "core (rectus abdominis)"]
    },
    "Military Press": {
        "primary_muscles": ["shoulders (deltoids)", "triceps (triceps brachii)"],
        "secondary_muscles": ["core (rectus abdominis)", "traps (trapezius)", "chest (pectoralis major)"]
    }
}
