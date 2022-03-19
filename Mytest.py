s=''
print(s[0:1])

ps='*'
print(ps.lower())
for i in range(4,len(ps)):
    print(p[i])
print('***')
print(all(ps[i]=='*' for i in range(4,len(ps))))

print(int(9/2))

M={'1':9,'2':4,'5':2,'10':3}
print(M)

s='I am a student'
print(s[::-1])
M={0:1,1:2}
print(M[3])

a={'a':1,'b':2,'c':3}
print(len(a))

print(chr(0x21))

print(ord('0'))
print(ord('9'))

print(8/11)


print(1/2+1/5+1/37+1/4070)

a='3'
a.isalnum()

print(a.isalnum())
for i in range(10):
    print(i)
    break
print(i)

j=0
while j<10:
    j+=1
print(j)

print(type([]) is list)
data=[{'id':'1','val':'a','level':1,'ord':1,'parent':'0'}, {'id':'11','val':'b','level':2,'ord':1,'parent':'1'}, {'id':'12','val':'c','level':2,'ord':2,'parent':'1'}]
print(data[0]['val'])



# def isprime(n):  #判断n是不是素数，素数只能被1和自己整除
#     m=int(n**(1/2))+1
#     for i in range(2,m,1):
#         if n % i == 0:
#             return 0
#     return 1
#
# print(isprime(9))
# for i in range(9):
#     for j in range(9):
#         print(i,j)

#数字颠倒
'''输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001'''
# a=int(input())
# #1516000
# b=''
# while a!=0:
#     b= b + str(a % 10)
#     a=int(a/10)
# print(b)

#字符串反转
# a=input()
# print(a[::-1])
# while a[i]!="/":
#     b+=a[]

#句子逆序
#I am a boy
# #方法1
# a=input()
# b=['']
# k=0
# for v in a:
#     b[k] += v
#     if v==' ':
#         b.append('')
#         k+=1
# print(''.join(b[::-1]))
# #方法2
# a=input()
# b =a.split(' ')
# print(' '.join(b[::-1]))


#字典排序
'''
9
cap
to
cat
card
two
too
up
boat
boot
'''
# try:
#     n = int(input())
#     b = []
#     for i in range(n):
#         b.append(input())
#         pass
#     for i in sorted(b):
#         print(i)
# except:
#     pass

#求int型正整数在内存中存储时1的个数
# raw_input = int(input())
# print(raw_input)
# count = 0
# while raw_input != 0:
#     if raw_input & 1 != 0:
#         count += 1
#     raw_input = raw_input >> 1
# print(count)


#购物单

# 如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
#     设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
# v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
#     请你帮助王强设计一个满足要求的购物单。
'''
输入：
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0

1500 7
500 1 0
400 4 0
300 5 1
400 5 1
200 5 0
500 4 0
400 4 0
'''
# t={}
# t['主']=[]
# t['主'].append([5,6,7])
# t['主'].append([1,2,3])
# print(t['主'])

import numpy as np
a=input().split(' ')
N=int(a[0])  #总钱数，购买物品总钱数不得超过此值
m=int(a[1])  #想购买物品的总数

col=3
t={}
t['主']=[]
t['从']=[]
for i in range(m):
    # print(input().split(' '))
    tmp=[int(v) for v in input().split(' ')]
    if tmp[2]==0:
        t['主'].append(tmp)
    else:
        t['从'].append(tmp)
        tmp.append(0)
# t['从']=np.array(t['从'])
# t['主']=np.array(t['主'])
s=0
Money=0
PriceList=[]
Price=999999999
ret=[]
idx=-1
for v in t['主']:
    if v[0]>price:
        continue
    if Money + v[0]>N:
        PriceList.append(v[0])
        price=min(PriceList)
        Money = 0
        s = 0
        l1=len(t['从'])
        for k in range(l1):
            t['从'][k][3] = 0
        continue
    Money = Money + v[0]
    s=s+v[0]*v[1]
    ret.append(s)
    idx+=1
    l=idx
    for m in t['从']:
        if Money+m[0]>N:
            PriceList.append()
            continue
        Money = Money + m[0]
        s=s+m[0]*m[1]
        ret.append(s)
        m[3]=1
        idx+=1
    # if idx==l:
    #     s=0
    #     Money=0
print(ret)
ret.sort(reverse=True)
print(ret[0])





