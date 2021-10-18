"""
Author: Arsene Bwasisi
Description: This program constructs a list of mutual friends between 
             two given name. It does this by creating an objects of individuals
             from a given file of names and and their friends. Then given two
             individuals, it finds friends that they have in common and returns
             that as a linked list. 
"""

from list_node import *

def create_dic(names, dic):
    """
    Create a dictionary from filename that includes all the names
    in the file as the key, and a list of people their are friends
    with as the value.
    Returns: The dictionary with added keys and values
    names: A list of name from the filename file
    dic: The dictionary bieng updated
    """

    if names[0] in dic:
        dic[names[0]].append(names[1])
    if names[1] in dic:
        dic[names[1]].append(names[0])
    if names[0] not in dic:
        dic[names[0]] = [names[1]]
    if names[1] not in dic:
        dic[names[1]] = [names[0]]
        
    return dic
    
def create_obj(key, value):
    """ 
    Use the Person class to create an object with the keys and values
    of the friends_dic. Initializes the object with the key
    (name of individual), then creates a linked list of the
    individuals friends using the set_friends() and add_friend() methods.
    Returns: An instance from the Person class, that includes the _name
    and _friends attributes
    key: Key from friends_dic
    value: Value from friends_dic
    """
    
    obj = Person(key)
    obj.set_friends(value[0])
    
    for friend in value[1:]:
        obj.add_friend(friend)
        
    return obj
    
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

def construct_relationships(filename):
    """
    Function will take in a file and organize the data into a dictionary
    to be processed. It will create a objects using the Person class and
    return a linked list of those objects.
    Returns: A linked list of instances returned by create_obj() function.
    filename: A file containing the data of pair of friends.
    """
    
    people = None
    friends_dic = dict()

    filename = open(filename, 'r')
    
    for line in filename:
        names = line.split()
        # updated friends_dic with the create_dic() function
        friends_dic = create_dic(names, friends_dic)

    for key, value in friends_dic.items():
        # create objects using the create_obj() function
        obj = create_obj(key, value)
        
        if people is None:
            people = ListNode(obj)  # initialize the first node
            cur = people
        else:
            cur.next = ListNode(obj)  # add remaining nodes
            cur = cur.next
    
    return people
    
def find_mutual_friends(friend_rels, name1, name2):
    """ 
    Function will look for name1 and name2 in the friends_rels list
    and if both names are in the list, it will use the get_friends()
    method, to get their list of friends and then it will use the 
    list_intersection() function to find mutual friends.
    Returns: A linkeds list of mutual friends of name1 and name2,
    returns none if either names isn't in list or no mutual friends
    are found
    friends_rels: The list returned by construct_relationships()
    name1: First given name
    name1: Second given name
    """
    
    cur1 = friend_rels
    
    while friend_rels is not None:
        if friend_rels.val.get_name() == name1:

            # Use the get_friends() method to grab the list
            # of friends of name1 and name2
            head1 = friend_rels.val.get_friends() 

            while cur1 is not None:
                if cur1.val.get_name() == name2:
                    head2 = cur1.val.get_friends()

                    # Use list_intersection, if both names in friends_rels,
                    # to find mutual friends
                    return list_intersection(head1, head2)
                    
                cur1 = cur1.next
                
            break
            
        friend_rels = friend_rels.next
    
    # If names not found in friends_rels...                
    return None
    
class Person:
    """ 
    This class creates an object for an individual and creates a list
    of friends they have.
    attributes: _name, _friends
    methods: get_name(return name of individual), get_friends
    (return friends list), set_name(sets the name of individual), set_friends
    (initialize friends list), and add_friends(adds to friends list).
    """
    
    def __init__(self, name):
        self._name = name
        self._friends = None
        
    def get_name(self):
        return self._name
        
    def get_friends(self):
        return self._friends
        
    def set_name(self, new_name):
        self._name = new_name
        
    def set_friends(self, friend):
        self._friends = ListNode(friend)
        self.cur = self._friends
    
    def add_friend(self, new_friend):
        self.cur.next = ListNode(new_friend)
        self.cur = self.cur.next
        
def main():
    
    file = 'in10.txt'
    filename = open(file, 'r')
    rel_list = construct_relationships(filename)
    mutual = find_mutual_friends(rel_list, 'Ethan', 'Miguel')
    print()
    print(mutual)

if __name__ == "__main__":
    main()