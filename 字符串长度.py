'''计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。

输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。
输入：
hello nowcoder
'''
# str=input()
# k=0  #计数器
# for v in str:
#     if v==' ':
#         k=0
#         continue
#     k+=1
# print(k)

##97-a  65-A
# string=input()
# a=input()
# a=a.upper()
# count=0
# for v in string:
#     if v.upper()==a:
#         count+=1
# print(count)

'''明明的随机数
描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据(用于不同的调查)，希望大家能正确处理)。


注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。

当没有新的输入时，说明输入结束。

输入描述：
注意：输入可能有多组数据(用于不同的调查)。每组数据都包括多行，第一行先输入随机整数的个数N，接下来的N行再输入相应个数的整数。具体格式请看下面的"示例"。

输入：
3
2
2
1
11
10
20
40
32
67
40
20
89
300
400
15
'''
def mysort(arr):
    for n in sorted(list(set(arr))):
        print(n)


import sys

#
# def mysort(arr):
#     for n in sorted(list(set(arr))):
#         print(n)
#
#
# while True:
#     try:
#         num = int(input())
#         arr = []
#         for i in range(num):
#             arr.append(int(input()))
#         mysort(arr)
#     except:
#         break


'''字符串分隔
描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

输入描述：
连续输入字符串(输入多次,每个字符串长度小于100)

输出描述：
输出到长度为8的新字符串数组

输入：
abc
123456789
'''
#方法一
# while True :
#     try:
#         s=input()
#         l=len(s)
#         k=0
#         while l>0:
#             #ret += '\r\n'
#             ret=''
#             for i in range(k,8+k):
#                 try:
#                     ret += s[i]
#                 except:
#                     ret+='0'
#             l=l-8
#             k+=8
#             print(ret)
#     except:
#         break
# #方法二
# def zero(n,s):
#     for i in range(n):
#         s+='0'
#     return s
# while True:
#     try:
#         s=input()
#         l=len(s)
#         while l>8:
#             print(s[:8])
#             s=s[8:]
#             l=len(s)
#         print(zero(8-l,s))
#     except:
#         break
'''进制转换
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
输入：
0xA
0xAA
0x76E
'''
#方法一
# m={str(i):i for i in range(10)}
# m.update({'A':10,'B':11,'C':12,'D':13,'E':14,'F':15})
# while True:
#     try:
#         s=input()
#         ret=0
#         s=s[2:]
#         for i in range(len(s)):
#             ret+=m[s[-(i+1)]]*16**i
#         print(ret)
#     except:
#         break
#方法二
# s=input()
# print(int(s,16))

'''质数因子
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

输入描述：
输入一个long型整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入：
180
复制
输出：
2 2 3 3 5
'''
