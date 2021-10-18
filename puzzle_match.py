"""
Author: Arsene Bwasisi
Description: This program will compare two values in lists left
             and right, top and bottom to check for any matches.
             it specifically looks for the reversed value in the 
             other list.
             
"""

def puzzle_match_LR(left,right):
    """ 
    Fucntion looks at value in the left list and checks whether its
    the same as the reversed version of a value in right list.
    """
    
    if left[1] == right[3][::-1]: # [::-1] returns the reversed value
        return True
                
    return False
    
def puzzle_match_TB(top,bot):
    """ 
    Fucntion looks at value in the top list and checks whether its
    the same as the reversed version of a value in bot list.
    """
    
    if top[0] == bot[2][::-1]:
        return True
                
    return False
    

def main():
    
    left = ['asd', '123', 'foo', 'bar']
    right = ['frd', 'wlm', 'bny', '321']
    
    top = ['xyz', 'az1', 'xxA', 'pyt']
    bot = ['xxA', 'cpp', 'lup', 'har']
    
    bool_2 = puzzle_match_LR(left,right)
    bool_2 = puzzle_match_TB(top,bot)

if __name__ == "__main__":
    main()
