from list_node import * 

def first_node(cur, new):
    
    nxt = cur.next
    cur.next = new
    new = cur
    cur = nxt
    
    return cur, new

def last_node(cur, new):
    
    nxt = cur.next
    if cur.next is not None:
        cur.next = None
    new.next = cur
    cur = nxt
    
    return cur, new

def middle_node(cur, new):
    
    nxt = new.next
    nxt2 = cur.next
    if cur.next is not None:
        cur.next = None
    new.next = cur
    new.next.next = nxt
    cur = nxt2
    
    return cur, new
    

def insertion_sort(head):
    
    sorted_list = None
    cur = head
    count = 0
    
    print('head:', cur)
    print('new:', sorted_list)
    print()
    
    while cur is not None:
        
        if count == 0:
            cur, sorted_list = first_node(cur, sorted_list)
            count += 1
        
        elif count == 1:
            if cur.val > sorted_list.val:
                cur, sorted_list = first_node(cur, sorted_list)
            else:
                cur, sorted_list = last_node(cur, sorted_list)
            
            count += 1
            
        elif count >= 2:
            temp = sorted_list
            count2 = 0
           
            while temp is not None:
                if cur.val > temp.val:
                    if count2 == 0:
                        cur, sorted_list = first_node(cur, sorted_list)
                        count += 1
                        
                        break
                    elif count2 >= 1:
                        smaller = temp.val
                        temp2 = sorted_list
                        while temp2 is not None:
                            if temp2.next.val is smaller:
                                cur, temp2 = middle_node(cur, temp2)
                                count += 1
                                
                                break
                                
                            temp2 = temp2.next
                            
                        break
                    
                elif temp.next is None:
                    cur, temp = last_node(cur, temp)                
                    count += 1
                        
                    break
                        
                count2 += 1
                temp = temp.next
                
        print('head:', cur)
        print('new:', sorted_list)
        print()
        
    head = sorted_list
    return head
        
def main():
    
    a = [5,1,2,0,4]
    head = ListNode(3)
    
    cur = head
    for n in a:
       
        cur.next = ListNode(n)
        cur = cur.next
       
    new = insertion_sort(head)

if __name__ == "__main__":
    main()  
    