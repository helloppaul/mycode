'''
N 位同学站成一排，音乐老师要请其中的 (N - K) 位同学出列，使得剩下的 K 位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为 1，2…，K ，他们的身高分别为 T1，T2，…，TK ，   则他们的身高满足存在 i （1<=i<=K） 使得 T1<T2<......<Ti-1<Ti>Ti+1>......>TK 。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

dp[i]:第i位同学，左侧的最多人数
dp[i]=max(dp[i-1],
第i个人左侧两种情况，要么出，要么不出
出：第i-1个同学比第i个同学高，出列

-------
8
186 186 150 200 160 130 197 200
~
4
-----
初始化 dp[i]=1

dp[1]=1

dp[2]=
if a[1]<a[2],则保留，dp[1]+1
if a[1]>=a[2], max(dp[1]+1,dp[2])

dp[3]=
if a[2]<a[3],则保留，dp[2]+1
if a[2]>a[3],则，max(dp[2]+1,dp[3])

dp[i]=max(dp[i-1]+1,dp[i])
'''
def leftmax(arr,n):
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[j]<arr[i] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
    return dp
while True:
    try:
        n=int(input())
        nums=list(map(int,input().split(' ')[:n]))
        dp_l=leftmax(nums,n)
        dp_r=leftmax(nums[::-1],n)[::-1]
        dp=[m+v for m,v in zip(dp_l,dp_r)]
        print(n-(max(dp)-1))
    except:
        break

