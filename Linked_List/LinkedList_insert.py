class Node:
        def __init__(self,key):
              self.key=key
              self.next=None

              
def insertend(head,x):
    tmp = Node(x)
    if head==None:
        return tmp
    curr=head
    while(curr.next!=None):
        curr=curr.next
    curr.next=tmp
    return head