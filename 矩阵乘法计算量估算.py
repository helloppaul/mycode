#s：待解析的括号字符串 idx：字符串起始下标 res：结果集
def findparis(s,idx,res):
    s_ = ''
    k=idx
    while k <len(s):
        if s[k] == '(' :
            t=findparis(s,k+1,res)
            s_+=t[0]
            k=t[1]
        elif s[k]==')':
            bidx = ord(s_[0]) - 65
            cidx = ord(s_[1]) - 65
            B,C=nlist[bidx],nlist[cidx]
            res.append(B[0] * B[1] * C[1])
            nlist[cidx]=[B[0],C[1]]
            return [s_[1],k]
        else:
            s_+=s[k]
        k+=1
while True:
    try:
        n=int(input())
        nlist=[]
        for i in range(n):
            nlist.append(list(map(int,input().split(' '))))
        s=input()
        res=[]
        findparis(s, 0, res)
        print(sum(res))
    except:
        break
'''
7
47 45
45 31
31 20
20 35
35 59
59 42
42 28
(A((B(C(DE)))(FG)))
~
3
50 10
10 20
20 5
(A(BC))
~
5
23 61
61 59
59 34
34 56
56 35
(A(((BC)D)E))
'''



# #s：待解析的括号字符串 idx：字符串起始下标 res：结果集
# def findparis(s,idx,res):
#     s_ = ''
#     k=idx
#     while k <len(s):
#         if s[k] == '(' :
#             t=findparis(s,k+1,res)
#             if t[0]!='':
#                 res.append(t[0])
#             k=t[1]
#             if s[k+1:k+2]!=')' and s[k+1:k+2]!='(':
#                 s_+=')'
#         elif s[k]==')':
#
#             return [s_,k]
#         else:
#             s_+=s[k]
#         k+=1