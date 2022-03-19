'''编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。

如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。

如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y

#$Y^!#Pf&~#FUyTtAfZhCs&Dly%M@(muOI@Le^mydvc((w$x-cP&t-f$R%CCp)bCck@P-ag
#$A^!#ab&~#CccCCCcDdef&Fff%g@(hIkl@LM^mmOPP((p$P-Rs&T-t$t%Uuv)wxYy@y-yZ

输入：
A Famous Saying: Much Ado About Nothing (2012/8).

输出：
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
'''
# def mpsort(lst,lim1,lim2):   #冒泡 从小到大
#     while True:
#         flag=1
#         for i in range(len(lst)-1):
#             if lst[i+1]>lst[i]:
#                 tmp=lst[i+1]
#                 lst[i+1]=lst[i]
#                 lst[i]=tmp
#                 flag=0
#         if flag==1:
#             break
map={'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y','Z':'Z','a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y','z':'Z'}
while True:
    try:
        s=input()
        lst=[v for v in s]
        res=''
        ln=len(s)
        while True:
            flag=1
            for i in range(ln-1):
                if lst[i] not in map:
                    continue
                for j in range(i+1,ln):
                    if lst[j] in map:
                        if map[lst[j]]<map[lst[i]]:
                            tmp=lst[j]
                            lst[j]=lst[i]
                            lst[i]=tmp
                            flag=0
                        break
            if flag == 1:
                res = ''.join(lst)
                break
        print(res)
    except:
        break

'''效率优化版'''
# map={'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y','Z':'Z','a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y','z':'Z'}
# while True:
#     try:
#         s=input()
#         lst=[v for v in s]
#         res=''
#         ln=len(s)
#         while True:
#             flag=1
#             i=0
#             while i < ln-1:
#                 if lst[i] not in map:
#                     i+=1
#                     continue
#                 for j in range(i+1,ln):
#                     if lst[j] in map:
#                         if map[lst[j]]<map[lst[i]]:
#                             tmp=lst[j]
#                             lst[j]=lst[i]
#                             lst[i]=tmp
#                             flag=0
#                         break
#                 i=j
#             if flag == 1:
#                 res = ''.join(lst)
#                 break
#         print(res)
#     except:
#         break