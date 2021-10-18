"""
Author: Arsene Bwasisi
Description: This program takes in a linked list and returns 
             its length using recursion.
"""

from list_node import *

def list_length(head):
    """ Return length of head."""

    if head is None:
        return 0
    return 1 + list_length(head.next)
    
def main():
    a = [10,15,20,25,30]
    
    head = ListNode(5)
    cur = head
    
    for n in a:
        cur.next = ListNode(n)
        cur = cur.next
    
    print(head)
    l = list_length(head)
    print(l)

if __name__ == "__main__":
    main()