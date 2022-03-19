'''
8
186 186 150 200 160 130 197 200
~
4

dp_l[i]:最长升序子序列，长度为i时，升序子序列末尾元素最小值
dp_r[j]:最长降序子序列，长度为j时，降序子序列末尾元素最大值
'''
def rightbound(arr,find,L=None):
    Larr=L if L else len(arr)
    left=0
    right=Larr
    while left < right :
        mid=int((left+right)/2)
        if arr[mid]==find:
            right=mid
        elif arr[mid]<find:
            left=mid+1
        elif find<arr[mid]:
            right=mid
    if left==0 or nums[left-1]!=find:
        return left
    return left-1

def leftmax(nums,n):
    dp_l=[nums[0]]
    dp_r=[nums[-1]]
    dp=[[],[]]
    k=0
    p=0
    for i in range(n):
        if dp_l[k]<nums[i]:
            dp_l.append(nums[i])
            k+=1
        else:
            idx=rightbound(dp_l,nums[i],k+1)
            dp_l[idx]=nums[i]
        dp[0].append(k + 1)

    for j in range(n-1,-1,-1):
        if dp_r[p]<nums[j]:
            dp_r.append(nums[j])
            p+=1
        else:
            idx=rightbound(dp_r,nums[j],p+1)
            dp_r[idx]=nums[j]
        dp[1].insert(0,p + 1)

    Max=dp[0][0]+dp[1][0]
    for i in range(1,n):
        if dp[0][i]+dp[1][i]>Max:
            Max=dp[0][i]+dp[1][i]
    return Max-1

while True:
    try:
        n=int(input())
        nums=list(map(int,input().split(' ')[:n]))
        print(n-leftmax(nums,n))
    except:
        break