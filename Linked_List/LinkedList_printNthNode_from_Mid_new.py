def printNthNodefromTail(head,n):
    if head==None:
        return 
    cnt = 0
    curr = head
    while curr.next!=None:
        cnt +=1
        curr = curr.next
    
    curr=head 
    for i in range(cnt-n+1):
        curr=curr.next
    print(curr.data)