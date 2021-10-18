"""
Author: Arsene Bwasisi
Description: This program will take in two linked list that are sorted
             in descending order and return a merged linked list that 
             is also sorted.
"""

from list_node import *

def first_node(cur, new):
    '''
    A function that adds a node at the beginning of the list.
    If the node being added is larger than the head of merge,
    this function is called.
        return:the cur pointer minus the added node
        return: the merged list with the new node
        cur: A list of nodes being added to merge
        new: The merge list that will take in a new node
    '''

    nxt = cur.next  # save next nodes
    cur.next = new  # cur head point to new(merge list)
    new = cur
    cur = nxt

    return cur, new

def last_node(cur, new):
    '''
    A function that adds a node at the end of the list.
    If the node being added is smaller than smallest node
    in merge, this function is called.
        return:the cur pointer minus the added node
        return: the merged list with the new node
        cur: A list of nodes being added to merge
        new: The merge list that will take in a new node
    '''

    nxt = cur.next
    if cur.next is not None:
        cur.next = None  # remove nodes after cur.head
    new.next = cur
    cur = nxt

    return cur, new

def middle_node(cur, new):
    '''
    A function that adds a node at the middle of the list.
    If the node being added is larger than one node
    but smaller than another, this function is called.
        return:the cur pointer minus the added node
        return: the merged list with the new node
        cur: A list of nodes being added to merge
        new: The merge list that will take in a new node
    '''

    nxt = new.next
    nxt2 = cur.next
    if cur.next is not None:
        cur.next = None  # creat space for new node
    new.next = cur
    new.next.next = nxt
    cur = nxt2

    return cur, new

def merge(list1, list2):
    '''
    This function takes two lists and merges them in to one
    linked list. The list is returned in sorted descending order
        return:a merged linked list(None if both list are None)
        list1: First linked list
        list2: Second linked list
    '''

    if list1 is None:
        return list2

    merged = list1

    while list2 is not None:
        temp = merged
        count = 0

        while temp is not None:
            if list2.val > temp.val:
                if count == 0:
                    list2, merged = first_node(list2, merged)
                    break

                elif count >= 1:
                    smaller = temp.val
                    temp2 = merged

                    # look for node before smaller
                    # add cur inbetween
                    while temp2 is not None:
                        if temp2.next.val is smaller:
                            list2, temp2 = middle_node(list2, temp2)
                            break

                        temp2 = temp2.next

                    break

            elif temp.next is None:
                list2, temp = last_node(list2, temp)
                break

            temp = temp.next
            count += 1

    return merged

def main():

    merged_list = merge(list1, list2)
    print(merged_list)

if __name__ == "__main__":
    main() 