class Node:
        def __init__(self,key):
              self.key=key
              self.next=None



def printn(head):
    if head==None:
        return 
    curr=head
    while curr!=None:
        print(curr.key)
        curr=curr.next