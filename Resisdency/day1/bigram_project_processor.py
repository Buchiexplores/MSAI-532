from collections import Counter
import re

# Load the file and read text
file_path = "Nyt.200811.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Step 1: Tokenize by word (convert to lowercase, remove punctuation)
words = re.findall(r'\b\w+\b', text.lower())  # Extract words, convert to lowercase

# Step 2: Create two word lists, off by one index
words1 = words[:-1]  # All words except the last one
words2 = words[1:]   # All words except the first one

# Step 3: Pair words to create bigrams
bigrams = list(zip(words1, words2))

# Step 4: Count bigrams
bigram_counts = Counter(bigrams)

# Step 5: Find and display the 10 most common bigrams
most_common_bigrams = bigram_counts.most_common(10)

# Print results
for bigram, count in most_common_bigrams:
    print(f"{bigram}: {count}")
