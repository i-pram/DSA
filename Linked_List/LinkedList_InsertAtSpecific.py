class Node:
        def __init__(self,key):
              self.key=key
              self.next=None


def insertpos(head,key,pos):
    tmp=Node(key)
    if head==None:
        tmp.next=head
        return head
    curr=head
    for i in range(pos-2):
        curr=curr.next
        if curr==None:
            return head
    tmp.next=curr.next
    curr.next=tmp