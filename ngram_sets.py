# Author: Arsene Bwasisi
# Description: This program takes a string and intenger and returns
#              a set of its n-gram

def ngram_sets(string, n):
    """ 
    Function uses n-gram algorithm to return a set of tuples with 
    length n, containg the values in string.
    """
    
    fields = string.split()
    startpos = 0
    ngram_set = set()
    
    # loop through list to get n-grams from the string parameter
    # convert n-grams to tuple and add to set
    # increment the start and end positon
    while n <= len(fields):
        sub_list = tuple(fields[startpos:n])
        ngram_set.add(sub_list)
        n += 1
        startpos += 1
        
    return ngram_set

def main():
    
    string = input("")
    n = 3
    ngram_sets(string, n)
    
if __name__ == "__main__":
    main()
    