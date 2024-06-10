def printMiddle_2(head):
    if head==None:
        return 
    slow = head
    fast = head
    while fast.next!=None and fast !=None:
        slow=slow.next
        fast = fast.next.next
    print(slow.data)