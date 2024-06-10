def search(head,x):
    if head==None:
        return 
    curr=head
    while curr!=None:
        if curr.key==x:
            return True
        curr=curr.next
    return False