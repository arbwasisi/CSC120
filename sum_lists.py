"""
Author: Arsene Bwasisi
Description: This program takes two linked lists and returns
             a linked list of where the nodes at the same index
             of both list are added.
"""

from list_node import *

def sum_lists(list1, list2):
    '''
    Funtion will loop through both list, and create a node from
    the sum of nodes in list1 and 2. If one node contains None it 
    will add value fro the other node, if both nodes are none it
    returns none.
        returns: None if both list are None, otherwise it returns the 
        summed list
        list1: First linked list
        list2: Second linked list
    '''

    # check None cases
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1 is None and list2 is None:
        return None
        
    sum_list = ListNode(list1.val+list2.val)
    cur = sum_list
    list1 = list1.next
    list2 = list2.next
    
    while True:
        
        if list1 is None:
            cur.next = list2
            break
        elif list2 is None:
            cur.next = list1
            break
        else:
            sum_val = list1.val + list2.val
            cur.next = ListNode(sum_val)
            cur = cur.next
            
            list1 = list1.next
            list2 = list2.next
            
            if list1 is None and list2 is None:
                break

    return sum_list

def main():
    
    sum_list = sum_lists(list1, list2)
    print(sum_list)

if __name__ == "__main__":
    main() 