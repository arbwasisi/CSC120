from list_node import * 

def reverse_list(head):
    
    new = None
    cur = head
    print('head:', cur)
    print('new:', new)
    print()
    
    while cur is not None:
        
        nxt = cur.next
        cur.next = new
        new = cur
        cur = nxt
        
        print('head:', cur)
        print('new:', new)
        print()
        
    return new
        
def main():
    
    a = [2,3]
    head = ListNode(1)
    cur = head
    for n in a:
       
        cur.next = ListNode(n)
        cur = cur.next
       
    new = reverse_list(head)

if __name__ == "__main__":
    main()