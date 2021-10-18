"""
Author: Arsene Bwasisi
Description: This program uses recursion to build triangular array
             of the size of a given number(num). The numbers in the 
             array are incremented from 1 to n. 
"""

def helper(array, inc):
    """
    Function takes an array containing the same value and it increment
    each value by inc.
    returns: An array that has been altered by incrementing its value.
    array: An array of size num, containing the last value of the
    previous sub list.
    inc: A number to increment each value by.
    """

    if array == []:
        return array
    array[0] += inc
    return array[:1] + helper(array[1:], inc+1)

def triangle2(num):
    """
    Function will create a triangular array, where the values within the
    list, are integers from 1 to n.
    returns: Triangular array.
    num: Size of the array.
    """
    
    if num == 0:
        return []

    if num == 1:
        return [[1]]
    # Traverse all the way down then work upwards
    array = triangle2(num-1)
    sub = helper([array[-1][-1]]*num,1)
    array += [sub]
    return array

def main():
    
    res = triangle2(4)
    for r in res:
        print(r)

if __name__ == "__main__":
    main()
    