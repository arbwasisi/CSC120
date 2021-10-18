"""
Author: Arsene Bwasisi
Description: This program takes two list and joins them together.
             One funtion joins them left to right, the other up and down.            
"""

def join_pieces_LR(left, right):
    """ Joins two list left and right into one list."""
    
    joint_list = []
    idx = 0
    
    for string in left:
        joint_str = string + right[idx]
        joint_list.append(joint_str)
        idx += 1
        
    return joint_list
    
def join_pieces_TB(top, bot):
    """ Joins two list top and bottom into one list."""

    for string in top:
        bot.append(string)

    return bot
    
    
def main():
    
    left = [' abc ', 'd   g', 'e   h', 'r   i', ' jkl ']
    right = [' 123 ', 'g   4', 'h   5', 'i   6', ' 789 ']
    
if __name__ == "__main__":
    main()