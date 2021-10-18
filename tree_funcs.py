from tree_node import*

def count(root):
    if root == None:
        return 0
    else:
        num = count(root.get_left()) + 1
        num2 = num + count(root.get_right())
   
    return num2
    
def is_bst(root):
    
    tree_val = in_order_traversal(root)
    return (tree_val == sorted(tree_val))
   
def search(root, val):
    if root == None:
        return
    elif val == root.get_val():
        return root
    elif root.get_left() is None and root.get_right() is None:
        return
    else:
        if root.get_left() is not None:
            lnode = root.get_left()
            node = search(lnode, val)
            if node is not None:
                return node
        if root.get_right() is not None:
            rnode = root.get_right()
            node = search(rnode, val)
            if node is not None:
                return node
                    
    return node
    
def bst_search(root, val):
    curr = root
    while curr is not None:
        if curr.get_val() == val:
            return curr
        elif curr.get_val() < val:
            curr = curr.get_right()
        else:
            curr = curr.get_left()
        
    return
    
def bst_insert(root, val):
    
    if root == None:
        return TreeNode(val)
    if val < root.get_val():
        lnode = root.get_left()
        lnode = bst_insert(lnode, val)
    elif val > root.get_val():
        rnode = root.get_right()
        rnode = bst_insert(rnode, val)
        
    return root
    
    
def pre_order_traversal(root):
    
    if root is None:
       return []
    else:
        array = [root.get_val()] + pre_order_traversal(root.get_left())
        array2 = array + pre_order_traversal(root.get_right())
    
    return array2
    
def post_order_traversal(root):
    
    if root is None:
       return []
    else:
        array = post_order_traversal(root.get_left())
        array2 = post_order_traversal(root.get_right()) + [root.get_val()]
        
    return array + array2
    
def in_order_traversal(root):
    
    if root == None:
        return []
    else:
        array = in_order_traversal(root.get_left()) + [root.get_val()]
        array2 = array + in_order_traversal(root.get_right())
   
    return array2

def main():
    x = [8,11,3,2,5,9]

if __name__ == "__main__":
    main() 