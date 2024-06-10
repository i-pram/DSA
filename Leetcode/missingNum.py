def missingnum(nums):
    l=[False]*(len(nums)+1)
    for i in nums:
        if i>=0 and i <=len(nums):
            l[i]=True
    for n in range(1,len(l)):
        if l[n]==False:
            return n
    return n+1