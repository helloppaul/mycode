def match(p,s):
    m,n=len(p),len(s)
    #dp[i][j]表示前i个模式和前j个字符串是否匹配
    #dp[i][0]:j=0表示空字符串，此时不确定是否匹配，如果是*则匹配，否则不能匹配(因为通配符可以匹配任意个字符串，所以能匹配)
    dp=[[False]*(n+1) for j in range(m+1)]
    dp[0][0]=True #空模式 空字符串匹配成功
    for i in range(1,m+1):
        if p[i-1]=='*':
            dp[i][0]=True
        else:
            break
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[i-1]=='*':
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            elif p[i-1]=='?' and s[j-1].isalnum():
                dp[i][j]=dp[i-1][j-1]
            elif p[i-1].lower()==s[j-1].lower():
                dp[i][j]=dp[i-1][j-1]
    return dp[m][n]

while True:
    try:
        ps,s=input(),input()
        print('true') if match(ps,s) else print('false')
    except:
        break