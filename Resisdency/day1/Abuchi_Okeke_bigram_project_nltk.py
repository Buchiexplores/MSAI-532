# Resisdency Day 1:Bigram Project
# Abuchi Godswill Okeke 
# School of Computer and Information Sciences, University of the Cumberlands
# MSAI532 - M51 Natural Language Processing
# Dr. Toni Farley
# January 31st, 2025

import nltk
from nltk.util import bigrams
from collections import Counter
import re

# Ensure the necessary NLTK tokenizer package is available
nltk.download('punkt')

# Load the file and read text
file_path = "Nyt.200811.txt"
output_file = "output.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Step 1: Tokenize by word (convert to lowercase, remove punctuation)
words = nltk.word_tokenize(text.lower())  # Tokenizes words while handling punctuation

# Step 2: Filter out punctuation tokens (ensuring only words are considered)
words = [word for word in words if re.match(r'\b\w+\b', word)]  # Keep only words

# Step 3: Generate bigrams using NLTK's bigrams function
bigrams_list = list(bigrams(words))

# Step 4: Count bigrams and find the 10 most common bigrams
bigram_counts = Counter(bigrams_list)
most_common_bigrams = bigram_counts.most_common(10)

# Result: Write results to an output file
with open(output_file, "w", encoding="utf-8") as out_file:
    for bigram, count in most_common_bigrams:
        out_file.write(f"{bigram}: {count}\n")

print(f"Results saved in {output_file}")

# Print results
for bigram, count in most_common_bigrams:
    print(f"{bigram}: {count}")
