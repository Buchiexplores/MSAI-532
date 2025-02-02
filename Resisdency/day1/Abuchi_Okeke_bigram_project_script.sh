#!/bin/bash

# Resisdency Day 1:Bigram Project
# Abuchi Godswill Okeke 
# School of Computer and Information Sciences, University of the Cumberlands
# MSAI532 - M51 Natural Language Processing
# Dr. Toni Farley
# January 31st, 2025

#1. Tokenize by word.
tr -s '[:space:]' '\n' < Nyt.200811.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' > words.txt

#2. Create two almost-duplicate files of words, off by one line, using tail.
tail -n +1 words.txt > words1.txt
tail -n +2 words.txt > words2.txt

#3. Paste them together so as to get word(i) and word(i +1) on the same line.
paste words1.txt words2.txt > bigrams.txt

#4. Count bigrams and find the 10 most common bigrams, format as tuples
sort bigrams.txt | uniq -c | sort -nr | head -10 | awk '{print "('"'"'" $2 "'"'"', '"'"'" $3 "'"'"'): " $1}'



