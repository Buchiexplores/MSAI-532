import nltk

# Download required NLTK data packages (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# List of sentences with provided tokens and tags in "word/tag" format
sentences = [
    "I/PRP need/VBP a/DT flight/NN from/IN Atlanta/NN",
    "Does/VBZ this/DT flight/NN serve/VB dinner/NNS",
    "I/PRP have/VB a/DT friend/NN living/VBG in/IN Denver/NNP",
    "Can/VBP you/PRP list/VB the/DT nonstop/JJ afternoon/NN flights/NNS"
]

# Process each sentence
for sentence in sentences:
    # Split into individual word/tag pairs and extract tokens and tags
    tokens_with_tags = sentence.split()
    provided_tokens = []
    provided_tags = []
    
    for token in tokens_with_tags:
        word, tag = token.rsplit('/', 1)
        provided_tokens.append(word)
        provided_tags.append(tag)
    
    # Reconstruct the raw sentence for automatic tagging
    raw_sentence = " ".join(provided_tokens)
    
    # Use NLTK to tokenize and tag the reconstructed sentence
    tokens = nltk.word_tokenize(raw_sentence)
    predicted_tags = nltk.pos_tag(tokens)
    # Compare provided tags with predicted tags and record all discrepancies
    errors = []
    for (provided_word, provided_tag), (predicted_word, predicted_tag) in zip(zip(provided_tokens, provided_tags), predicted_tags):
        if provided_tag != predicted_tag:
            errors.append((provided_word, provided_tag, predicted_tag))
    
    # Output the results
    print(f"Sentence: {raw_sentence}")
    if errors:
        for error in errors:
            print(f"Potential tagging error for word '{error[0]}': provided tag = {error[1]}, predicted tag = {error[2]}")
    else:
        print("No tagging errors found.")
    print()  # Blank line between sentences
