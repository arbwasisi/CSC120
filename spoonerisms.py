"""
Author: Arsene Bwasisi
Description: This program will read in various phrases, break them down 
             into their underlying sounds (called “phonemes”), and then 
             swap sounds between two words to new generate. It will use
             a dictionary of words and their phonemes to do this.
"""

import sys

def swap_words(word_1, word_2, words, idx_1, idx_2):
    """
    Function will swap the orginal words in the phrase with
    the new generated words.
    return: A 2d list of all the new phrase from the swap of two words
    word_1: List of all words found from the first word's swap
    word_2: List of all words found from the second word's swap
    words: A list which contains the inputed phrase
    idx_1: The index of the first word from the phrase
    idx_2: The index of the second word from the phrase
    """
    
    new_phrases = []
        
    for string_1 in word_1:
        for string_2 in word_2:
            copy = words[:]
            copy[idx_1] = string_1
            copy[idx_2] = string_2
                
            new_phrases.append(copy)

    return new_phrases

def find_words(swap_1, swap_2, phonemes, words, idx_1, idx_2):
    """
    Function will find all words in the phonemes dictionary from the
    given list of swaps.
    return: 2d list from the swap_word function
    swap_1: List of phonemes from first word, that has a swapped sound
    word_2: List of phonemes from second word, that has a swapped sound
    words: A list which contains the inputed phrase
    idx_1: The index of the first word from the phrase
    idx_2: The index of the second word from the phrase
    """
    
    word_1 = []
    word_2 = []
    
    for word, array in phonemes.items():
        if swap_1 in array:
            word_1.append(word)
        if swap_2 in array:
            word_2.append(word)
    
    if len(word_1) > 0 and len(word_2) > 0:
        phrases = swap_words(word_1, word_2, words, idx_1, idx_2)
    
        return phrases
    
def swap_sounds(sounds_1, sounds_2, phonemes, words, pos_1, pos_2):
    """
    Function recieve a list of phonemes from two words, and swap every
    phoneme from one word with a phoneme in the other
    return: A 2d list of all new phrase from the original phrase 
    sounds_1: A 2d list of phonemes from first word
    sounds_2: A 2d list of phonemes from second word
    words: A list which contains the inputed phrase
    pos_1: The index of the first word from the phrase
    pos_2: The index of the second word from the phrase
    """
    
    new_phrases = []
    
    # this loops through each 2d list to make all
    # possible combinations for swapping letters
    for sub_1 in sounds_1:
        idx_1 = 0
        for sound_1 in sub_1:
            swap_1 = sub_1[:]
            for sub_2 in sounds_2:
                idx_2 = 0
                for sound_2 in sub_2:
                    swap_2 = sub_2[:]
                    if sound_1 != sound_2:
                        swap_1[idx_1] = sound_2
                        swap_2[idx_2] = sound_1
                
                        phrases = find_words(swap_1, swap_2,\
                        phonemes, words, pos_1, pos_2)

                        if phrases != None:
                            new_phrases += phrases
                        
                    idx_2 += 1
        
            idx_1 += 1
            
    return new_phrases
        
def build_spoonersisms(phonemes, words):
    """
    Function loop through a inputed phrase and pass two words
    into the swap_word function.
    return: A 2d list of all new phrase from all user input
    phonemes: dictionary from the pronounciation dictionary file
    with a word as the key and 2d list of phonemes as values
    words: A list which contains the inputed phrase
    """

    spoonerism = []
    idx_1 = 0
    idx_2 = 1

    # while the first index is not the last word loop
    # through and grab two words to perform a task on
    while words[idx_1] is not words[-1]:
        if words[idx_1].upper() in phonemes and\
        words[idx_2].upper() in phonemes:

            sounds_1 = phonemes[words[idx_1].upper()]
            sounds_2 = phonemes[words[idx_2].upper()]

            phrases = swap_sounds(sounds_1, sounds_2,\
            phonemes, words, idx_1, idx_2)
            spoonerism += phrases

        if words[idx_2] is words[-1]:
            idx_1 += 1
            idx_2 = idx_1 + 1
        else:
            idx_2 += 1
            
    return spoonerism
    
def convert(spoonerisms):
    """
    This function will convert the 2d list of spoonerism phrases
    into a list of strings of all the spoonerisms
    return: A list of constructed spoonerisms
    spoonerisms: A 2d list of all spoonerisms from user input 
    """
    
    new_spoons = []
    
    for phrase in spoonerisms:
        convert_phrase = ''
        for word in phrase:
            if word is not phrase[-1]:
                convert_phrase += word.upper() + ' '
            else:
                convert_phrase += word.upper()
        
        if convert_phrase not in new_spoons:
            new_spoons.append(convert_phrase)
        
    return new_spoons
    
def print_spoons(spoonerism, phrase):
    """
    This function will print the result of the swapped phonemes
    return: None
    spoonerisms: A 2d list of all spoonerisms from user input
    phrase: A list of the user input that has been split and stripped
    """

    print('Phrase: ', end='')
    
    for word in phrase:
        if word is not phrase[-1]:
            print(word.upper(), '', end='')
        else:
            print(word.upper())
    
    for string in spoonerism:
        print(' ', string)
    
    

def process_input(user_input, phoneme_dic):
    """
    This function will process the given input, strip and punctuation
    on either end of a word, and pass the input into the build_spoonerism
    function.
    return: A list of the sorted, printable spoonerisms
    return: The input that has been stripped and split
    user_input: A phrase inputed by the user that will be processed
    phoneme_dic: The dictionary from the pronounciation dictionary file
    """

    chars = ['.', ',', ';', ':', '!', '?', '-', '(', ')', '"', "'"]
    strip_words = []
    split_line = user_input.split()

    for word in split_line:
        while word[-1] in chars:
            word = word.strip(word[-1])

        while word[0] in chars:
            word = word.strip(word[0])

        strip_words.append(word)

    spoonerism = build_spoonersisms(phoneme_dic, strip_words)
    new_spoons = convert(spoonerism)
    sorted_spoons = sorted(new_spoons)
    
    return sorted_spoons, strip_words

        
def create_dic(file):
    """
    This function create a dictionary from an inputed file which includes
    a link to a pronounciation dictionary.
    return: The created dictionary, with words being the key and sounds 
    being the value
    file: Link to the file to be open
    """
    
    open_file = open(file, 'r')

    phonemes = dict()
    for line in open_file:
        sounds = []
        split_line = line.split('  ')
        # Check for any repeated words
        if split_line[0] in phonemes:
            phonemes[split_line[0]].append(split_line[1].split())
        else:
            sounds.append(split_line[1].split())
            phonemes[split_line[0]] = sounds
            
    return phonemes
    
def main():
    
    input_file = input()
    dic = create_dic(input_file)
    
    for line in sys.stdin:
        if line != '\n':
            spoons, phrase = process_input(line, dic)
        
            print_spoons(spoons, phrase)

main()