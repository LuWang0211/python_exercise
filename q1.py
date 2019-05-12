#!/usr/bin/env python3
# Copyright 2018 Lulu Wang
import os

## input file 
def words_count_file(count_file):
    lines = []

    with open(count_file,"r") as f:
        for line in f:
            lines.append(line)

    word_count(lines)

## input text
def words_count_text(text):
    lines = text.split("\n")
    word_count(lines)

## Count 
def word_count(lines):
    
    words_num        = 0
    unique_words_num = 0
    sentences_num    = 0

    ## Total word count    
    for line in lines:
        words = line.split()
        words_num += len(words)

    print(f"Total word count: {words_num}")

    ## Unique words count
    unique_word = {}
  
    for line in lines:
        words = line.split()
        for word in words:
            cleaned_word = word.replace(".", "")
            cleaned_word = cleaned_word.replace(",", "")
            cleaned_word = cleaned_word.replace("!", "")
            cleaned_word = cleaned_word.replace("?", "")
            cleaned_word = cleaned_word.lower()

            if cleaned_word not in unique_word:
                unique_word[cleaned_word] = 1
                unique_words_num = unique_words_num + 1
            else:
                unique_word[cleaned_word] = unique_word[cleaned_word] + 1

    print(f"Unique words: {unique_words_num}" )

    # Sentence
    all_text = "".join(lines)
    sentences        = all_text
    stops_num        = sentences.count(".")
    questions_num    = sentences.count("?")
    exclamatory_num  = sentences.count("!")
    sentences_num    = stops_num + questions_num + exclamatory_num

    print(f"Sentences:{sentences_num}")

    # List of word used
    reverse_word_count_to_word = {}
    count_array = []

    for key in unique_word:        
        count = unique_word[key]

        if count not in reverse_word_count_to_word:
            reverse_word_count_to_word[count] = []
            reverse_word_count_to_word[count].append(key)
            count_array.append(count)
        else:
            reverse_word_count_to_word[count].append(key)

    count_array.sort()
    count_array.reverse()

    for count in count_array:
        print(f"Words {reverse_word_count_to_word[count]} appeared {count} times")

## Input:accept input from text or file
my_input = input("Enter a txt file name or a text content: ")
if '.txt' in my_input: 
    count_number  = words_count_file(my_input)
else:
    count_number  = words_count_text(my_input)
