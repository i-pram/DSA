class Node:
        def __init__(self,key):
              self.key=key
              self.next=None


def sortedInsert(head,x):
    tmp=Node(x)
    if head==None:
        return tmp 
    elif head.data<x:
        tmp.next=head
        return tmp
    else:
        curr=head
        while curr.next!=None and curr.next.data<x:
            curr=curr.next
        tmp.next=curr.next
        curr.next=tmp
    return head