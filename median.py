# Author: Arsene Bwasisi
# Description: This program will take in a string as 
#			   input and find its median

string = input('')

def median(string):
    x = len(string)
    
    if x%2 != 0:
        i = int(x/2)
        print(string[i])
    else:
        i = int(x/2)
        print(string[i-1]+string[i])
        
median(string)