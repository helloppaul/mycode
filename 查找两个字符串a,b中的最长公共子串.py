'''查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
abcdefghijklmnop
abcsafjklmnopqrstuvw
--------------------
jklmnop
'''
while True:
    try:
        s1=input()
        s2=input()
        ls1 = len(s1)
        ls2 = len(s2)
        maxlen=0
        if ls1>ls2:
            s1,s2=s2,s1
            ls1,ls2=ls2,ls1
        for i in range(ls1):   #遍历短的字符串
            for j in range(i+1,ls1+1):
                sub=s1[i:j]
                if sub in s2 and (j-i)>maxlen:
                    maxstr=sub
                    maxlen=j-i
        print(maxstr)
    except:
        break