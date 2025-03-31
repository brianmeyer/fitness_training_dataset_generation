"""
Exercise definitions and ranges.
"""

EXERCISES = {
    "compound_barbell": {
        "exercises": [
            # Pressing movements
            "Bench Press", "Overhead Press", "Incline Bench Press", "Decline Bench Press",
            "Close Grip Bench Press", "Behind the Neck Press", "Floor Press",
            # Squat variations
            "Back Squat", "Front Squat", "Box Squat", "Pause Squat", "Safety Squat Bar Squat",
            "Zercher Squat", "Overhead Squat", "Split Squat", "Bulgarian Split Squat",
            # Deadlift variations
            "Conventional Deadlift", "Sumo Deadlift", "Romanian Deadlift", "Deficit Deadlift",
            "Block Pull", "Rack Pull", "Snatch Grip Deadlift", "Trap Bar Deadlift",
            # Row variations
            "Barbell Row", "Pendlay Row", "Meadows Row", "T-Bar Row", "Seal Row",
            "Bent Over Row", "Yates Row", "Power Row",
            # Other compound movements
            "Power Clean", "Power Snatch", "High Pull", "Good Morning", "Landmine Press",
            "Landmine Row", "Landmine Squat", "Zercher Carry", "Farmer's Carry"
        ],
        "weight_range": (45, 405),  # in lbs
        "rep_range": (1, 12),
        "set_range": (3, 5),
        "rpe_range": (6, 9)
    },
    "compound_dumbbell": {
        "exercises": [
            # Pressing movements
            "Dumbbell Press", "Incline Dumbbell Press", "Decline Dumbbell Press",
            "Dumbbell Shoulder Press", "Arnold Press", "Seated Dumbbell Press",
            "Floor Press", "Dumbbell Push Press", "Dumbbell Push Jerk",
            # Squat variations
            "Goblet Squat", "Bulgarian Split Squat", "Dumbbell Front Squat",
            "Dumbbell Walking Lunge", "Dumbbell Step-up", "Dumbbell Box Step-up",
            "Dumbbell Split Squat", "Dumbbell Romanian Deadlift",
            # Row variations
            "Dumbbell Row", "Dumbbell Renegade Row", "Dumbbell Meadows Row",
            "Dumbbell Single Arm Row", "Dumbbell High Pull", "Dumbbell Upright Row",
            # Deadlift variations
            "Dumbbell Romanian Deadlift", "Dumbbell Stiff Leg Deadlift",
            "Dumbbell Sumo Deadlift", "Dumbbell Deficit Deadlift",
            # Other compound movements
            "Dumbbell Clean", "Dumbbell Snatch", "Dumbbell Thruster",
            "Dumbbell Swing", "Dumbbell Turkish Get-up", "Dumbbell Windmill",
            "Dumbbell Figure 8", "Dumbbell Halo", "Dumbbell Carry"
        ],
        "weight_range": (10, 100),
        "rep_range": (6, 15),
        "set_range": (3, 4),
        "rpe_range": (6, 8)
    },
    "isolation": {
        "exercises": [
            # Chest
            "Dumbbell Fly", "Cable Fly", "Pec Deck", "Chest Fly", "Incline Fly",
            "Decline Fly", "Cable Crossover", "Machine Fly",
            # Shoulders
            "Lateral Raise", "Front Raise", "Reverse Fly", "Face Pull", "Cable Lateral Raise",
            "Machine Lateral Raise", "Dumbbell Shrug", "Cable Shrug", "Machine Shrug",
            # Back
            "Straight Arm Pulldown", "Cable Pullover", "Machine Pullover",
            "Reverse Grip Pulldown", "Close Grip Pulldown", "Wide Grip Pulldown",
            # Biceps
            "Bicep Curl", "Hammer Curl", "Preacher Curl", "Concentration Curl",
            "Incline Dumbbell Curl", "Spider Curl", "Cable Curl", "Machine Curl",
            "Reverse Curl", "Zottman Curl", "Cross Body Curl",
            # Triceps
            "Tricep Extension", "Skull Crusher", "Overhead Extension", "Cable Extension",
            "Machine Extension", "Rope Extension", "Close Grip Push-up", "Diamond Push-up",
            "Tricep Kickback", "Tricep Pushdown", "Single Arm Extension",
            # Legs
            "Leg Extension", "Leg Curl", "Calf Raise", "Seated Calf Raise",
            "Standing Calf Raise", "Machine Calf Raise", "Donkey Calf Raise",
            "Hip Abduction", "Hip Adduction", "Inner Thigh", "Outer Thigh",
            "Machine Leg Press", "Machine Hack Squat", "Machine Squat",
            # Core
            "Cable Crunch", "Machine Crunch", "Ab Crunch", "Reverse Crunch",
            "Hanging Leg Raise", "Cable Woodchop", "Russian Twist", "Side Plank",
            "Plank", "Mountain Climber", "Flutter Kick", "Bicycle Crunch",
            # Forearms
            "Wrist Curl", "Reverse Wrist Curl", "Wrist Extension", "Wrist Flexion",
            "Farmer's Carry", "Plate Pinch", "Towel Pull-up", "Dead Hang",
            # Glutes
            "Hip Thrust", "Glute Kickback", "Machine Hip Thrust", "Cable Hip Thrust",
            "Banded Hip Thrust", "Glute Bridge", "Single Leg Hip Thrust",
            # Lower Back
            "Back Extension", "Machine Back Extension", "Cable Back Extension",
            "Reverse Hyperextension", "Machine Reverse Hyper"
        ],
        "weight_range": (5, 50),
        "rep_range": (10, 20),
        "set_range": (3, 4),
        "rpe_range": (6, 8)
    },
    "bodyweight": {
        "exercises": [
            # Upper Body Push
            "Push-up", "Incline Push-up", "Decline Push-up", "Diamond Push-up",
            "Wide Push-up", "Close Grip Push-up", "Pike Push-up", "Handstand Push-up",
            "Dips", "Bench Dips", "Ring Dips", "Pseudo Planche Push-up",
            # Upper Body Pull
            "Pull-up", "Chin-up", "Neutral Grip Pull-up", "Wide Grip Pull-up",
            "Close Grip Pull-up", "L-Sit Pull-up", "Muscle-up", "Inverted Row",
            "Australian Pull-up", "Ring Row", "Bodyweight Row",
            # Core
            "Plank", "Side Plank", "Hollow Hold", "Arch Hold", "Superman Hold",
            "L-Sit", "Hanging Leg Raise", "Toes to Bar", "Knee to Elbow",
            "Mountain Climber", "Flutter Kick", "Bicycle Crunch", "Russian Twist",
            # Lower Body
            "Bodyweight Squat", "Pistol Squat", "Jump Squat", "Split Squat",
            "Bulgarian Split Squat", "Walking Lunge", "Reverse Lunge",
            "Step-up", "Box Jump", "Broad Jump", "Calf Raise",
            # Full Body
            "Burpee", "Mountain Climber", "Bear Crawl", "Crab Walk",
            "Inchworm", "Spider-man Crawl", "Animal Flow", "Handstand Walk",
            # Gymnastic Movements
            "Handstand", "L-Sit", "Front Lever", "Back Lever", "Planche",
            "Muscle-up", "Skin the Cat", "Human Flag", "Handstand Push-up"
        ],
        "weight_range": (0, 45),  # For weighted variations
        "rep_range": (5, 20),
        "set_range": (3, 5),
        "rpe_range": (6, 8)
    },
    "machine": {
        "exercises": [
            # Upper Body Push
            "Machine Chest Press", "Machine Incline Press", "Machine Decline Press",
            "Machine Shoulder Press", "Machine Military Press", "Machine Seated Press",
            "Machine Dip", "Machine Tricep Extension", "Machine Pec Deck",
            # Upper Body Pull
            "Lat Pulldown", "Machine Row", "Seated Row", "Cable Row", "Machine Pullover",
            "Machine High Row", "Machine Low Row", "Machine Reverse Fly",
            "Machine Back Extension", "Machine Reverse Hyperextension",
            # Arms
            "Machine Bicep Curl", "Machine Tricep Extension", "Machine Preacher Curl",
            "Cable Bicep Curl", "Cable Tricep Extension", "Cable Lateral Raise",
            "Cable Front Raise", "Cable Face Pull", "Cable Shrug",
            # Lower Body
            "Leg Press", "Hack Squat", "Smith Machine Squat", "Machine Leg Extension",
            "Machine Leg Curl", "Machine Calf Raise", "Machine Hip Thrust",
            "Machine Hip Abduction", "Machine Hip Adduction", "Machine Inner Thigh",
            "Machine Outer Thigh", "Machine Glute Kickback", "Machine Back Extension",
            # Core
            "Machine Ab Crunch", "Machine Torso Rotation", "Machine Woodchop",
            "Cable Crunch", "Cable Woodchop", "Cable Pull-through",
            # Specialty Machines
            "Cable Crossover", "Cable Fly", "Cable Pullover", "Cable Lateral Raise",
            "Cable Front Raise", "Cable Shrug", "Cable Upright Row", "Cable Face Pull",
            "Cable Tricep Pushdown", "Cable Bicep Curl", "Cable Tricep Extension",
            "Cable Crunch", "Cable Woodchop", "Cable Pull-through"
        ],
        "weight_range": (20, 300),  # Machine plates typically range from 5-45 lbs per side
        "rep_range": (8, 20),
        "set_range": (3, 4),
        "rpe_range": (6, 8)
    },
    "kettlebell": {
        "exercises": [
            # Dynamic Movements
            "Kettlebell Swing", "Kettlebell Snatch", "Kettlebell Clean",
            "Kettlebell Clean and Jerk", "Kettlebell Thruster", "Kettlebell Jerk",
            "Kettlebell Push Press", "Kettlebell Push Jerk", "Kettlebell Long Cycle",
            # Squat Variations
            "Kettlebell Goblet Squat", "Kettlebell Front Squat", "Kettlebell Rack Squat",
            "Kettlebell Overhead Squat", "Kettlebell Split Squat", "Kettlebell Bulgarian Split Squat",
            "Kettlebell Box Squat", "Kettlebell Pistol Squat",
            # Deadlift Variations
            "Kettlebell Deadlift", "Kettlebell Romanian Deadlift", "Kettlebell Sumo Deadlift",
            "Kettlebell Stiff Leg Deadlift", "Kettlebell Single Leg Deadlift",
            # Pressing Movements
            "Kettlebell Press", "Kettlebell Push Press", "Kettlebell Push Jerk",
            "Kettlebell Floor Press", "Kettlebell Military Press", "Kettlebell Arnold Press",
            # Row Variations
            "Kettlebell Row", "Kettlebell Renegade Row", "Kettlebell Single Arm Row",
            "Kettlebell Meadows Row", "Kettlebell High Pull", "Kettlebell Upright Row",
            # Complex Movements
            "Kettlebell Turkish Get-up", "Kettlebell Windmill", "Kettlebell Figure 8",
            "Kettlebell Halo", "Kettlebell Arm Bar", "Kettlebell Bottoms Up Press",
            # Lunge Variations
            "Kettlebell Walking Lunge", "Kettlebell Reverse Lunge", "Kettlebell Step-up",
            "Kettlebell Box Step-up", "Kettlebell Cossack Squat",
            # Core and Stability
            "Kettlebell Plank", "Kettlebell Side Plank", "Kettlebell Suitcase Carry",
            "Kettlebell Rack Carry", "Kettlebell Overhead Carry", "Kettlebell Waiter Carry",
            # Dynamic Complexes
            "Kettlebell Flow", "Kettlebell Circuit", "Kettlebell Complex",
            "Kettlebell EMOM", "Kettlebell Tabata", "Kettlebell AMRAP"
        ],
        "weight_range": (10, 100),  # Common kettlebell weights
        "rep_range": (5, 20),
        "set_range": (3, 5),
        "rpe_range": (6, 8)
    },
    "olympic": {
        "exercises": [
            # Main Lifts
            "Clean", "Clean and Jerk", "Snatch", "Power Clean", "Power Snatch",
            "Split Clean", "Split Jerk", "Push Jerk", "Push Press",
            # Squat Variations
            "Front Squat", "Back Squat", "Overhead Squat", "Behind the Neck Squat",
            "Split Squat", "Pause Squat", "Box Squat", "Safety Squat Bar Squat",
            # Pulling Variations
            "Clean Pull", "Snatch Pull", "High Pull", "Deadlift", "Clean Deadlift",
            "Snatch Deadlift", "Deficit Deadlift", "Block Pull", "Rack Pull",
            # Hang Variations
            "Hang Clean", "Hang Snatch", "High Hang Clean", "High Hang Snatch",
            "Low Hang Clean", "Low Hang Snatch", "Block Clean", "Block Snatch",
            # Jerk Variations
            "Split Jerk", "Push Jerk", "Power Jerk", "Behind the Neck Jerk",
            "Push Press", "Military Press", "Behind the Neck Press",
            # Assistance Lifts
            "Clean Grip Deadlift", "Snatch Grip Deadlift", "Romanian Deadlift",
            "Good Morning", "Back Extension", "Reverse Hyperextension",
            # Technical Drills
            "Clean High Pull", "Snatch High Pull", "Clean Extension",
            "Snatch Extension", "Clean Recovery", "Snatch Recovery",
            # Complexes
            "Clean + Jerk", "Snatch + Overhead Squat", "Clean + Front Squat",
            "Clean + Push Press", "Snatch + Overhead Squat", "Clean + Jerk + Front Squat"
        ],
        "weight_range": (95, 405),  # Olympic lifting weights
        "rep_range": (1, 5),  # Olympic lifts typically use lower reps
        "set_range": (3, 6),
        "rpe_range": (7, 9)  # Olympic lifts typically use higher RPE
    }
}