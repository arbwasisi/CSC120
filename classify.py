# Author: Arsene Bwasisi
# Description: This program will take in a string as 
#			   input and classify it as a vowel, consonant or neither

word = input('')
vowel = ['a', 'e', 'i', 'o', 'u']

def classify_string(word):
    if word[0].lower() in vowel:
        print('vowel')
    elif word[0].lower().isalpha():
        print('consonant')
    else:
        print('neither')

classify_string(word)
