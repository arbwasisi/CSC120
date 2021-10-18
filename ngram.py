# Author: Arsene Bwasisi
# Description: This program takes a list as input, a starting position
#              and a length and returns a list from that postion of 
#              that lenght

def ngram(arglist, startpos, length):
    """ Function will return n-gram of arglist"""
    
    # define the end postion as the sum of the length
    # and starting postion
    endpos = startpos + length 
    
    # if endpos is 0 slice to end of list
    if endpos == 0:
        return arglist[startpos:]
    else:
        # if endpos is out of range return empty list
        if endpos > len(arglist):
            return list()
        else:
            return arglist[startpos:endpos]
    
def main():
    
    arglist = input('')
    startpos = input('')
    length = input('')

    ngram(arglist, startpos, length)

if __name__ == "__main__":
    main()
