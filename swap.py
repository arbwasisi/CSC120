# Author: Arsene Bwasisi
# Description: This program will take in a string as input and
#              swap the end of the string with the beginning.

string = input('')

def swap_characters(string):
    x = len(string)

    if x%2 != 0:# check for odd value
        i = int(x/2)# get the middle character
        if x == 1:
            print(string)
        else:
            swapped = string[-i:] + string[i] + string[:i]
            print(swapped)
    else:
        i = int(x/2)
        swapped = string[-i:] + string[:i]
        print(swapped)

swap_characters(string)