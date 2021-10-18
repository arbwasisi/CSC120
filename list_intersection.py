"""
Author: Arsene Bwasisi
Description: This program takes two linked list and creates a list
             from their intersections.      
"""

from list_node import *
    
def list_intersection(head1, head2):
    """
    Return linked list of the intersection of head1 and head2
    head1: First linked list
    head2: Second linked list
    """

    retval = None

    while head1 is not None:
        cur = head2
        while cur is not None:
            if head1.val == cur.val:

                # initialize the first node
                if retval is None:
                    retval = ListNode(cur.val)
                    copy = retval

                # Add node to list
                else:
                    copy.next = ListNode(cur.val)
                    copy = copy.next
                    
                break
                    
            cur = cur.next
            
        head1 = head1.next
        
    return retval
    
def main():
    
    a = [10,15,20,25,30]
    b = [20,30,40]
    
    head1 = ListNode(5)
    head2 = ListNode(10)
    cur1 = head1
    cur2 = head2
    
    for n in a:
        cur1.next = ListNode(n)
        cur1 = cur1.next
        
    for n in b:
        cur2.next = ListNode(n)
        cur2 = cur2.next
    
    new = list_intersection(head1, head2)
    print(new)
    
if __name__ == "__main__":
    main()