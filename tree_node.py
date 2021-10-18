class TreeNode:
    def __init__(self, val):
        self._val = val
        self._lnode = None
        self._rnode= None
        
    def get_val(self):
        return self._val
        
    def get_left(self):
        return self._lnode
        
    def get_right(self):
        return self._rnode
        
    def set_left(self, val):
        self._lnode = val
        
    def set_right(self, val):
        self._rnode = val   
        
    def search(self, val):
        
        if val == self._val:
            return self
        elif self._lnode is None and self._rnode is None:
            return
        else:
            if self._lnode is not None:
                node = self._lnode.search(val)
                if node is not None:
                    return node
            if self._rnode is not None:
                node = self._rnode.search(val)
                if node is not None:
                    return node
                    
        return node
        
    def bst_search_loop(self, val):
        
        curr = self
        while curr is not None:
            if curr._val == val:
                return curr
            elif curr._val < val:
                curr = curr._rnode
            else:
                curr = curr._lnode
        
        return
        
    def bst_insert_loop(self, val):
        
        curr = self
        if curr is None:
            return TreeNode(val)
        else:
            while curr is not None:
                if val < curr._val:
                    if curr._lnode is None:
                        curr._lnode = TreeNode(val)
                        break
                    else:
                        curr = curr._lnode
                else:
                    if curr._rnode is None:
                        curr._rnode = TreeNode(val)
                        break
                    else:
                        curr = curr._rnode

def main():
    x = [8,11,3,2,5,9]

if __name__ == "__main__":
    main() 