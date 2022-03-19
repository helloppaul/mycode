'''
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符
注意：匹配时不区分大小写。
'''
def ismatch(ps,s,i,j):
    if i>len(ps)-1 and j>len(s)-1: #两个字符串同时结束，表示匹配成功
        return True
    if i>len(ps)-1 or j>len(s)-1:   #其中有一个字符串先结束，则匹配失败
        return False
    if s[j] not in M:
        return False

    if ps[i]=='?':
        return ismatch(ps, s, i+1, j+1)
    elif ps[i]=='*':
        isbreak=0
        for k in range(i+1,len(ps)):
            if ps[k]!='*':
                isbreak=1
                break
        if isbreak==1:
            k-=1
        else:
            k=i
        return ismatch(ps, s, k + 1, j) or ismatch(ps, s, k + 1, j + 1) or ismatch(ps, s, k, j + 1)
        # if ismatch(ps, s, i + 1, j) or ismatch(ps, s, i + 1, j + 1) or ismatch(ps, s, i, j + 1):
        #     return 1
    elif ps[i]==s[j].lower() or ps[i]==s[j].upper():
        return ismatch(ps, s, i + 1, j+1)
    return False

M={'H', 'z', 'p', 'L', 'A', 'Q', 'u', 'v', 'i', 'B', 'r', 'y', '1', 't', 'j', 'm', 'W', '5', 'k', 'C', 'G', 'Z', 'e', 'O', '8', 'T', 'b', 'q', 'V', 'x', 'n', 'P', '7', 'E', 'I', 'Y', 'h', 'N', 's', 'F', 'd', 'U', '2', '0', 'a', 'w', 'X', 'S', 'K', 'g', 'l', 'R', '3', 'c', 'o', 'f', '9', 'J', '4', '6', 'M', 'D'}
while True:
    try:
        ps,s=input(),input()
        flag=1
        ls=len(s)
        lps=len(ps)
        print('true')if ismatch(ps,s,0,0) else print('false')
    except:
        break
'''
te?t*123
text1234
false

te?t*.*
txt12.xls
false

**Z
0QZz
true
'''