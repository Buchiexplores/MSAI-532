import spacy

#requirements
#!pip install spacy 
#!python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")

# 1. Original sentence (grammatically correct) related to the course and Walmart:
sentence = "Learning NLP helps me excel as a software engineer at Walmart."
doc = nlp(sentence)

print("Original sentence POS tags:")
for token in doc:
    print(f"{token.text:20s} {token.pos_}")

# 2. Introduce 3 spelling errors: "Learning" -> "Lerning", "software" -> "softwre", "engineer" -> "engneer"
sentence_misspelled = "Lerning NLP helps me excel as a softwre engneer at Walmart."
doc_misspelled = nlp(sentence_misspelled)

print("\nModified sentence (with spelling errors) POS tags:")
for token in doc_misspelled:
    print(f"{token.text:20s} {token.pos_}")
