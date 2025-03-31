# Fitness Workout Dataset Generator

A Python-based tool for generating a high-quality dataset of fitness workout data, including individual exercises and complete training sessions. The dataset is designed for training AI models to provide intelligent workout analysis and recommendations.

## Features

- Generates both individual exercise and complete training session examples
- Parallel processing for efficient dataset generation
- Checkpoint system to resume interrupted generation
- Quality validation of generated responses
- Rate limiting and error handling for API calls
- Comprehensive exercise and muscle data

## Project Structure

```
.
├── data/               # Exercise and muscle data
│   ├── exercises.py   # Exercise definitions and variations
│   ├── feedback.py    # Feedback templates
│   └── muscles.py     # Muscle group definitions
├── generators/        # Generation logic
│   ├── exercise.py   # Exercise example generation
│   ├── prompts.py    # Prompt templates
│   └── session.py    # Session example generation
├── utils/            # Utility functions
│   ├── api.py       # API interaction
│   ├── checkpoint.py # Checkpoint management
│   ├── quality.py   # Response validation
│   └── rate_limiter.py # Rate limiting
├── generate_dataset.py # Main script
└── requirements.txt   # Python dependencies
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

Run the dataset generation script:
```bash
python generate_dataset.py
```

The script will:
- Generate 3000 exercise examples and 2000 session examples
- Process examples in parallel using available CPU cores
- Save progress to checkpoint.json
- Output results to fitness_workout_dataset.jsonl

## Output Format

The generated dataset is in JSONL format, with each line containing a JSON object with:
- `text`: The workout data in a structured format
- `reasoning`: Analysis of the workout's effectiveness
- `recommendation`: Specific advice for improvement

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 