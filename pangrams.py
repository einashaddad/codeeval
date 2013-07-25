'''
Pangrams - CodeEval
https://www.codeeval.com/open_challenges/37/

The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet. Such sentences are called pangrams. You are to write a program, which takes a sentence, and returns all the letters it is missing (which prevent it from being a pangram). You should ignore the case of the letters in sentence, and your return should be all lower case letters, in alphabetical order. You should also ignore all non US-ASCII characters.In case the input sentence is already a pangram, print out the string NULL
'''

import sys

def pangrams(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'm', 'n', 'o', 
                'p','q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 
                'z']

    #remove all whitespace from sentence
    sentence = ''.join(sentence.split())

    #sort the set of lower case letters
    letters = sorted(set(sentence.lower()))
    print letters

    #iterate through the alphabet if does not exist in the sentence 
    #concatenate to the string missing
    missing = ''
    for letter in alphabet:
        if letter not in letters:
            missing += letter
    
    if missing:
        return missing
    return "NULL"

with open(sys.argv[1]) as f:
    for line in f:
        if line:
            print pangrams(line)
