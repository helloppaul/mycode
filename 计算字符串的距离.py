'''描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。

Ex：

字符串A:abcdefg

字符串B: abcdef

通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

要求：

给定任意两个字符串，写出一个算法计算它们的编辑距离。



本题含有多组输入数据。


输入描述：
每组用例一共2行，为输入的两个字符串

输出描述：
每组用例输出一行，代表字符串的距离

输入：
abcdefg
abcdef
abcde
abcdf
abcde
bcdef

输出：
1
1
2
'''

# def editDistance(str1, str2):
#     '''
#     计算字符串str1和str2的编辑距离
#     '''
#     edit = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 d = 0
#             else:
#                 d = 1
#             edit[i][j] = min(edit[i - 1][j] + 1, edit[i][j - 1] + 1, edit[i - 1][j - 1] + d)
#     return edit[len(str1)][len(str2)]
#
#
# while True:
#     try:
#         print(editDistance(input(), input()))
#     except:
#         break

def distance(s1,s2):
    len1=len(s1)+1
    len2=len(s2)+1
    edit=[[i+j for j in range(len2)] for i in range(len1)]
    for i in range(1,len1):
        for j in range(1,len2):
            if s1[i-1]==s2[j-1]:
                d=0
            else:
                d=1
            edit[i][j]=min(edit[i-1][j]+1,edit[i][j-1]+1,edit[i-1][j-1]+d)
    return edit[-1][-1]
while True:
    try:
        print(distance(input(), input()))
    except:
        break

# def editDistance(str1, str2):
#     '''
#     计算字符串str1和str2的编辑距离
#     '''
#     edit = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 d = 0
#             else:
#                 d = 1
#             edit[i][j] = min(edit[i - 1][j] + 1, edit[i][j - 1] + 1, edit[i - 1][j - 1] + d)
#     return edit[len(str1)][len(str2)]
#
#
# while True:
#     try:
#         print(editDistance(input(), input()))
#     except:
#         break