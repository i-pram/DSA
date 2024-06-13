from typing import List
def findDuplicates(self, nums: List[int]) -> List[int]:
    d=dict()
    ll=[]
    mx=0
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if d[i]>1:
            ll.append(i)
    if len(ll)>0:
        return ll
    else:
        return []
        