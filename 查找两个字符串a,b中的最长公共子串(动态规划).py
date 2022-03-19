'''查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
abcdefghijklmnop
abcsafjklmnopqrstuvw
--------------------
jklmnop
'''
while True:
    try:
        s1 = input()
        s2 = input()
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]   #dp[i][j]:字符串1在第i个位置 字符串2在第j个位置时，两者公共子串的长度
        index, max_len = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        index = i
                else:
                    dp[i][j] = 0   #表示在i,j位置时，两者没有公共子串，所以公共子串长度为0
        print(s1[index-max_len:index])
    except:
        break