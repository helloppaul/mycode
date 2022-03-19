'''放苹果(动态规划)
d[i][j]=d[i][j-1]+d[i-j][j]
i个苹果,j个盘子
d[0][j]=1
d[i][1]=1
'''

while True:
    try:
        m,n=list(map(int,input().split(' ')))
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][1]=1
        for j in range(n+1):
            dp[0][j]=1
            dp[1][j]=1
        for i in range(2,m+1):
            for j in range(2,n+1):
                if i<j:
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j]
        print(dp[m][n])
    except:
        break