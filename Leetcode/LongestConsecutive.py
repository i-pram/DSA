def longestConsecutive(nums):
    if len(nums)>0 and min(nums)<0:
        minus_numb=min(nums)
        nums = [x+abs(minus_numb) for x in nums]
    l=set(nums)
    s=[False]*(len(l)+1)
    for i in l:
        if i <= len(l):
            s[i]=True
    cnt=0
    print(s)
    for j in range(0,len(l)):
        if s[j]==s[j+1]==True:
            cnt +=1
        else:
            cnt=0
            # print(cnt)
    if len(l)==1:
        return 1
    elif len(l)==0:
        return 0
    elif len(l)>=2 and cnt>=1:
        return cnt+1
    else: 
        return 0