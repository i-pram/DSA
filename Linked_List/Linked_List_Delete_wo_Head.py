def deletewohead(ptr):
    tmp=ptr.next
    ptr.key=tmp.key
    ptr.next=ptr.next.next