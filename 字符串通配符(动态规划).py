
'''
**Z
0QZz
true
~
h*h*ah**ha*h**h***hha
hhhhhhhahhaahhahhhhaaahhahhahaaahhahahhhahhhahaaahaah
false
'''
def match(p,s):
    m,n=len(p),len(s)
    #dp[i][j]表示前i个模式和前j个字符串是否匹配
    #dp[0][j] 空模式无法匹配字符串；dp[i][0] 不确定，只有模式为*才能匹配空字符串
    dp=[ [False]*(n+1) for i in range(m+1)]
    dp[0][0]=True #空模式 空字符串匹配成功
    for i in range(1,m+1):
        if p[i-1]=='*':
            dp[i][0] = True
        else:
            break
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[i-1]=='*':  #当第i个通配符是*时，可选择匹配或者不匹配。
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            elif p[i-1]=='?' and s[j-1].isalnum():
                dp[i][j]=dp[i-1][j-1]
            elif s[j-1].lower()==p[i-1].lower():   #当第i个通配符和第j个字符串相等时，则前i个通配符和前j个字符串是否匹配等价于前i-1个通配符和j-1个字符串是否匹配
                dp[i][j]=dp[i-1][j-1]
    return dp[m][n]



M={'H', 'z', 'p', 'L', 'A', 'Q', 'u', 'v', 'i', 'B', 'r', 'y', '1', 't', 'j', 'm', 'W', '5', 'k', 'C', 'G', 'Z', 'e', 'O', '8', 'T', 'b', 'q', 'V', 'x', 'n', 'P', '7', 'E', 'I', 'Y', 'h', 'N', 's', 'F', 'd', 'U', '2', '0', 'a', 'w', 'X', 'S', 'K', 'g', 'l', 'R', '3', 'c', 'o', 'f', '9', 'J', '4', '6', 'M', 'D'}
while True:
    try:
        ps,s=input(),input()
        print('true') if match(ps,s) else print('false')
    except:
        break
'''
te?t*123
text1234
false
~
te?t*.*
txt12.xls
false
~
**Z
0QZz
true
'''