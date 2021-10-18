class DListNode:

    def __init__(self, val):

        self._val = val
        self._next = None
        self._prev = None
        
    def get_val(self):
        return self._val
    
    def get_next(self):
        return self._next
        
    def get_prev(self):
        return self._prev
        
    def set_val(self, val):
        self._val = val
        
    def set_next(self, val):
        self._next = val
        
    def set_prev(self, val):
        self._prev = val

def main():
    a = [10,15,20,25,30]
    
    head = DListNode(5)
    cur = head
    
    for n in a:
        cur.prev = cur
        cur.next = DListNode(n)
        cur = cur.next
    print(head.next.prev.val)
        

if __name__ == "__main__":
    main()