"""
Author: Arsene Bwasisi
Description: This program takes three linked lists and constructs 
             a new linked list by alternating between adding a node
             from list1 then list2 then list3, continuously.
"""

from list_node import *

def zipper3(list1, list2, list3):
    '''
    This function constructs a new list from three linked list,
    by alternating bewteen each node and adding it to the new list.
        return: The zippered linked list 
        list1: First linked list
        list2: Second linked list
        list3: Third linked list
    '''
    
    if list1 is None and list2 is None:
        return list3
    if list1 is None and list3 is None:
        return list2
    if list2 is None and list3 is None:
        return list1
    
    zippered = None

    # if first list is none, switch remaining
    # lists
    if list1 is None:
        cur1 = list2
        cur2 = list3
        cur3 = list1
    else:
        cur1 = list1
        cur2 = list2
        cur3 = list3
    count = 0

    while True:

        # count will determine which node from which
        # list to add
        if count == 0: 
            # set zippered to first list if not None
            if zippered is None:
                zippered = cur1
                cur1 = cur1.next
                temp = zippered
                if cur1 is None:
                    if cur2 is None:
                        temp.next = cur3
                    else:
                        temp.next = cur2
                count += 1
                continue

            else:
                # skip if a list is empty
                if cur1 is None:
                    count += 1
                    continue

                nxt = cur1.next
                # point to an available node
                # if none are available break loop
                if cur2 is None:
                    if cur3 is None:
                        break
                    else:
                        cur1.next = cur3
                else:
                    cur1.next = cur2

                temp.next = cur1
                cur1 = nxt

        elif count == 1:
            if cur2 is None:
                count += 1
                continue

            nxt = cur2.next
            if cur3 is None:
                if cur1 is None:
                    break
                else:
                    cur2.next = cur1
            else:
                cur2.next = cur3

            temp.next = cur2
            cur2 = nxt

        else:
            if cur3 is None:
                count = 0
                continue

            nxt = cur3.next
            if cur1 is None:
                if cur2 is None:
                    break
                else:
                    cur3.next = cur2
            else:
                cur3.next = cur1

            temp.next = cur3
            cur3 = nxt

        count += 1
        if count == 3:
            count = 0
        temp = temp.next

    return zippered

def main():


    zipped = zipper3(None, list1, list3)
    print(zipped)

if __name__ == "__main__":
    main()
