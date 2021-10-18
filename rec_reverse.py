"""
Author: Arsene Bwasisi
Description: This program will reverse a given linked list
             using recursion.
"""

from list_node import *

def reverse_list(head, tail):
    """ 
    Function adds a node from head backwards to produce a
    reverse list.
    head: A linked list
    tail: End of list
    """

    # place head pointer at tail of list
    nxt = head.next  # Save the next node
    head.next = tail

    if nxt is None:
        return head
    return reverse_list(nxt, head)
        
def rec_reverse(head):
    """ Return the reversed list from reverse_list."""

    if head is not None:
        return reverse_list(head, None)
    return head
    

def main():
    a = [10,15,20,25,30]
    
    head = ListNode(5)
    cur = head
    
    for n in a:
        cur.next = ListNode(n)
        cur = cur.next
    
    print(head)
    l = rec_reverse(head)
    print(l)

if __name__ == "__main__":
    main()