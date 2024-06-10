class Node:
        def __init__(self,key):
              self.key=key
              self.next=None


def inserthead(head,x):
    tmp = Node(x)
    if head==None:
        return tmp
    tmp.next=head
    return tmp