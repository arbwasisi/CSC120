"""
Author: Arsene Bwasisi
Description: This program takes two linked lists and constructs 
             a new linked list by alternating between adding a node
             from one list then the other continuously.
"""


from list_node import *

def position_node(cur1, cur2, new):
    '''
    This function postions the node in the zippered list for
    each alternative node in list1 and 2.
        returns: the cur pointer at list1 or 2
        returns: the list being constructed with the added node
        cur1: The node that will be pointing to another node
        cur2: The node being pointed at
    '''

    nxt = cur1.next
    cur1.next = cur2
    new.next = cur1
    cur1 = nxt

    return cur1, new

def zipper(list1, list2):
    ''' 
    Function will take in two list and alternate between adding a
    node from list1 into a new list, and adding a list from list2,
    in that order.
        return: constructed zipper list
        list1: First linked list
        list2: Second linked list
    '''

    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1 is None and list2 is None:
        return None

    zippered = None
    cur1 = list1
    cur2 = list2
    count = 0

    while True:

        # add node from list1 if count is even
        # else add node from list2
        if count%2 == 0:
            # set the first node to list1
            # unless list1 is None
            if count == 0:
                zippered = cur1
                cur1 = cur1.next
                if cur1 is None:
                    zippered.next = cur2
                    break
                temp = zippered
            else:
                cur1, temp = position_node(cur1, cur2, temp)

                if cur1 is None:
                    break
                temp = temp.next
        else:
            cur2, temp = position_node(cur2, cur1, temp)

            if cur2 is None:
                break
            temp = temp.next

        count += 1

    return zippered

def main():

    zipped = zipper(None, 111)
    print(zipped)

if __name__ == "__main__":
    main()