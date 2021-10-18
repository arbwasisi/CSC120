"""
Author: Arsene Bwasisi
Description: This program returns a square 2d list from the function
             square, which takes in as arguments, the size of the list,
             that starting value, and how much to increment.
             
"""

def square(size, start, inc):
    ''' Function wil return 2d list of lenght size by size.'''
    
    second_list = []
    count_1 = 0
    
    while count_1 < size:
        first_list = []
        count_2 = 0
        while count_2 < size:
            first_list.append(start)
            start += inc
            count_2 += 1
            
        second_list.append(first_list)
        start = first_list[1]
        count_1 += 1
        
    return second_list        
    

def main():
    
    size = int(input())
    start = int(input())
    inc = int(input())
    
    square(size, start, inc)
    
if __name__ == "__main__":
    main()