from transformers import pipeline

# Initialize the translation pipeline for English-to-Spanish translation
translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")

# Input sentence for translation
input_sentence = ("I am excited to attend the Natural Language Processing (MSAI-532-M51) class "
                  "because it offers cutting-edge insights into language models.")

# Translate the sentence
translated_output = translator(input_sentence)[0]['translation_text']

# Print the results
print("Input Sentence:", input_sentence)
print("Translated Output:", translated_output)
