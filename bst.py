"""
Author: Arsene Bwasisi
Description: This program uses the TreeNode class to create a binary 
             search tree. With a given tree a user can insert new nodes,
             find a path to a node, or find the lowest common node
             bewtween two noods in the tree.
"""


class TreeNode:
    """
    This class creates an object of a binary tree. Given a value,
    the class creates a node for the value as well as a light and
    right pointer.
    attributes: _val, _lnode, _rnode
    methods: 
    -insert(self, node): Takes in a value, and inserts it in the tree.
    -path(self, node): Returns a list of the values you traverse
    through to reach it including itself, returns None if node not in tree
    """

    def __init__(self, val):
        self._val = val
        self._lnode = None
        self._rnode= None
    
    def insert(self, node):
        
        # create a node if none exist
        if self._val == None:
            self._val = TreeNode(node)
        
        if self._val == node:
            return  # return None if node already exist
        elif self._val < node:
            if self._rnode is None:
                self._rnode = TreeNode(node)
            else:
                return self._rnode.insert(node)
        else:
            if self._lnode is None:
                self._lnode = TreeNode(node)
            else:
                return self._lnode.insert(node)
                
    def path(self, node):
        
        # Traverse down the list to find node
        # if node isn't found, return None
        if self._val == node:
            return [self._val]
            
        if self._val < node:
            if self._rnode == None:
                return
            else:
                retval = self._rnode.path(node)
        elif self._val > node:
            if self._lnode == None:
                return
            else: 
                retval = self._lnode.path(node)
        
        # After traverseing down tree, check the return value
        # to determine whether to return None, or an array
        if retval is None:
            return
        else:
            return [self._val] + retval
            
def mktree(array):
    """
    This function use TreeNode and its method insert() to create a tree.
    returns: A TreeNode object, None if array is empty.
    array: A list of value to add to the tree object.
    """

    if array != []:
        root = TreeNode(array[0])
    
        for n in array[1:]:
            root.insert(n)
        
        return root
        
        
def path(root, val):
    """
    Returns a Python list that gives the path, from the root to
    the node with value val.
    returns: List of values from root to node, None if node isn't in root
    root: A TreeNode object.
    val: Value to search in root.
    """
    
    if root != None:
        return root.path(val)
    
def find_lca(path1, path2, idx):
    """
    Function will take two list, recurse the list backwardly, and find
    values both list have in common.
    returns: The earliest common value at the tail of both list.
    path1: A list containing the path to a node(val1).
    path2: A list containing the path to a node(val2).
    idx: An interger that will act as an indices.
    """
    
    # Slice path1 till common value is found, if path1 is empty
    # no common value was found, thus return Non
    if path1 == []:
        return
    if path1[-1] == path2[idx]:
        return path1[-1]
    else:
        # When we are at the beginning of path2, reset the idx
        # and slice path1
        if path2[idx] == path2[0]:
            return find_lca(path1[:-1], path2, len(path2)-1)
        else:
            return find_lca(path1, path2, idx-1)
        
def lca(root, val1, val2):
    """
    Use find_lca() to find the lowest common value given two nodes
    and their path within the tree.
    returns: The lowest common value
    root: A TreeNode object.
    val1: First value to search in root.
    val2: Second value to search in root.
    """

    path1 = path(root, val1)
    path2 = path(root, val2)
    
    if path1 != None and path2 != None:
        return find_lca(path1, path2, len(path2)-1)
        
def main():
    x = [8,11,3,2,5,9]
    
    root = mktree(x)
    
    print(root.path(2))
    print(lca(root, 11,9))

if __name__ == "__main__":
    main()
    