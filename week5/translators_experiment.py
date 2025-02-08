from transformers import pipeline
import difflib
from deep_translator import GoogleTranslator

#Load 100 words of a sample text in English
def load_text_from_file(file_path, word_limit=100):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()[:word_limit]  # Extract first 100 words
        return " ".join(words)

#Load first 100 words from sample_english.txt
file_path = "sample_english.txt"  
selected_text = load_text_from_file(file_path,100)

# Translate from English to French
src_lang = "en"
tgt_lang = "fr"  


# Hugging Face Transformer Model (MarianMT)
model_1_name = "Helsinki-NLP/opus-mt-en-fr"

def translate_with_huggingface(text, model_name):
    translator = pipeline("translation_en_to_fr", model=model_name)
    translated = translator(text, max_length=200)
    return translated[0]['translation_text']

def translate_with_google(text, src, tgt):
    return GoogleTranslator(source=src, target=tgt).translate(text)

# Translate using Hugging Face model
translated_text_1 = translate_with_huggingface(selected_text, model_1_name)

# Translate using Google Translate
translated_text_2 = translate_with_google(selected_text, src_lang, tgt_lang)

# Compute differences using difflib with more context
differ = difflib.Differ()
diff = list(differ.compare(translated_text_1.split(), translated_text_2.split()))

# Format the differences more clearly
diff_analysis = []
for line in diff:
    if line.startswith('  '):  # Common words
        diff_analysis.append(f"SAME: {line[2:]}")
    elif line.startswith('- '):  # Words unique to HuggingFace
        diff_analysis.append(f"HuggingFace only: {line[2:]}")
    elif line.startswith('+ '):  # Words unique to Google
        diff_analysis.append(f"Google only: {line[2:]}")

# Prepare formatted difference output
diff_text = "\n".join(diff_analysis) if diff_analysis else "No significant differences found."

# Print results to console
print("\n--- Translation Comparison ---\n")
print(f"Original Text (First 100 words from sample.txt):\n{selected_text}\n")
print(f"Model 1 (Hugging Face - {model_1_name}):\n{translated_text_1}\n")
print(f"Model 2 (Google Translate API):\n{translated_text_2}\n")
print("Detailed Differences Analysis (Translation that appear in both models are marked as SAME\nwhile the ones that appear in only one model are marked as Google only or HuggingFace only):\n\n")
print("------------------------------Differences------------------------------\n")
print(diff_text)

# Save the comparison to a file
output_file = "translation_comparison.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Original Text (First 100 words from sample.txt):\n{selected_text}\n\n")
    f.write(f"Model 1 (Hugging Face - {model_1_name}):\n{translated_text_1}\n\n")
    f.write(f"Model 2 (Google Translate API):\n{translated_text_2}\n\n")
    f.write("Detailed Differences Analysis (Translation that appear in both models are marked as SAME\nwhile the ones that appear in only one model are marked as Google only or HuggingFace only):\n\n")
    f.write("------------------------------Differences------------------------------\n")
    f.write(diff_text)

print(f"\nComparison complete! Detailed analysis saved to {output_file}")