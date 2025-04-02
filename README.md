# Fitness Workout Dataset Generator

A Python-based tool for generating and cleaning a high-quality dataset of fitness workout data, including individual exercises and complete training sessions. The dataset is designed for training AI models to provide intelligent workout analysis and recommendations.

## Features

- **Dataset Generation:**
  - Generates both individual exercise examples and complete training session examples.
  - Utilizes parallel processing for efficient dataset generation.
  - Implements a checkpoint system to resume interrupted generation.
  - Validates generated responses for quality and consistency.
  - Handles rate limiting and errors for API calls.
  - Provides comprehensive exercise and muscle data.

- **Dataset Cleaning:**
  - Improves the generated workout data by refining the analysis and recommendation sections.
  - Leverages the Groq API to clean text artifacts (e.g., Chinese characters, cut-off recommendations, thinking process remnants).
  - Ensures a consistent output format with clear **Workout Data**, **Reasoning**, and **Recommendation** sections.
  - Uses multithreading and batch processing (with 5 worker threads) for efficient cleaning.
  - Maintains progress via a checkpoint file (`cleaning_checkpoint.json`) to resume cleaning if interrupted.

## Project Structure

```
.
├── data/                     # Exercise and muscle data
│   ├── exercises.py          # Exercise definitions and variations
│   ├── feedback.py           # Feedback templates
│   └── muscles.py            # Muscle group definitions
├── generators/               # Generation logic
│   ├── exercise.py           # Exercise example generation
│   ├── prompts.py            # Prompt templates
│   └── session.py            # Session example generation
├── utils/                    # Utility functions
│   ├── api.py                # API interaction
│   ├── checkpoint.py         # Checkpoint management
│   ├── quality.py            # Response validation
│   └── rate_limiter.py       # Rate limiting
├── generate_dataset.py       # Main script to generate dataset
├── clean_dataset.py          # Script to clean and improve dataset entries
├── cleaning_checkpoint.json  # Checkpoint file for the cleaning process
└── requirements.txt          # Python dependencies
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fitness-workout-dataset.git
cd fitness-workout-dataset
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
export GROQ_API_KEY=your_api_key_here  # On Windows: set GROQ_API_KEY=your_api_key_here
```

## Usage

1. Run the dataset generation script:
```bash
python generate_dataset.py
```
The script will:
- Generate 3000 exercise examples and 2000 session examples
- Process examples in parallel using available CPU cores
- Save progress to checkpoint.json
- Output results to fitness_workout_dataset.jsonl


### 2. Clean the Dataset

After generation, refine the workout data by running the cleaning script:

```bash
python clean_dataset.py
```
This script will:
- Read from fitness_workout_dataset.jsonl.
- Use the Groq API to improve the Reasoning and Recommendation sections.
- Process entries in batches using 5 worker threads.
- Maintain progress via cleaning_checkpoint.json for resuming the process.
- Output the cleaned dataset to fitness_workout_dataset_cleaned.jsonl.


## Output Format

Both the raw and cleaned datasets are in JSONL format. Each line contains a JSON object with the following fields:
- text: Contains the structured workout data, including:
- Workout Data: The original workout details.
- Reasoning: An evidence-based analysis with 2-3 key points.
- Recommendation: Clear, actionable advice with 2-3 specific recommendations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
