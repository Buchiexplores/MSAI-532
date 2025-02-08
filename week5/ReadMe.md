# Translation Model Comparison Experiment

A Python script that compares translations between Hugging Face's MarianMT model and Google Translate.

## Experiment Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Prepare your input:
   - Place your English text in `sample_english.txt`
   - The script will load and process the first 100 words

## Usage

Run the experiment:

```bash
python translators_experiment.py
```

## Output

The script will:
- Translate the text using both models
- Compare the translations
- Save results to `translation_comparison.txt`

## Models Used

- Hugging Face: Helsinki-NLP/opus-mt-en-fr
- Google Translate API

