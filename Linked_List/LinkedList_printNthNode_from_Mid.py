def printNthNodefromTail_2(head,n):
    if head==None:
        return 
    first=head 
    second=head
    for i in range(n):
        if first ==None :
            return
        first = first.next
    while first!=None:
        first=first.next
        second=second.next
    print(second.data)
    