'''
abcbaaa
~5
'''
while True:
    try:
        s=input()
        ls=len(s)
        Max=ls
        list=[]
        for j in range(ls-1,-1,-1):
            Max=j+1
            tmp=0
            for i in range(j):  #得到子串，计算每个子串的最长回文串
                k=j-i
                tmp += 2
                if i>=k:
                    break
                if s[i]!=s[k]:
                    Max-=tmp
                    tmp=0
            list.append(Max)
        print(max(list))
    except:
        break