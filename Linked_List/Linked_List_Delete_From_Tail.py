def deletefromtail(head):
    if head==None:
        return
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head