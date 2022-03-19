'''
6
2 5 1 5 4 5
:3
~
30
186 13 322 264 328 110 120 73 20 35 240 97 150 221 284 324 46 219 239 284 128 251 298 319 304 36 144 236 163 122
:10
dp[i]:走完前i个桩时，最多的步数
'''
while True:
    try:
        n=int(input())
        arr=list(map(int,input().split(' ')[:n]))
        dp=[1]*(n+1)
        dp[0]=0
        for i in range(2,n+1):
            for j in range(1,i):   #i前面的桩
                if arr[j-1]<arr[i-1]:   #如果i前面的某个桩(j)比i小，那么说明从j踩到第i个桩需要+1步.拿这个踩完之后的步数 dp[j] + 1 跟当前存储的最大步数 dp[i] 比较一下，选个大的放进去
                    dp[i]=max(dp[i],dp[j]+1)
        print(max(dp))
    except:
        break