'''
给出一个名字，该名字有26个字符组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。\
输入描述：
整数N，后续N个名字
输出描述：
每个名称可能的最大漂亮程度
输入：
2
zhangsan
lisi
输出：
2
zhangsan
lisi
'''
while True:
    try:
        n=int(input())
        slist=[]
        for i in range(n):
            slist.append(input())
        ltt=''
        for v in slist:
            M = {}
            for ltt in v:
                if ltt in M:
                    M[ltt]+=1
                else:
                    M[ltt]=1
            # 对统计的字母的次数从大到小排序
            lst = sorted(M.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            Max = 26
            r = 0
            for m in lst:
                r += Max * m[1]
                Max -= 1
            print(r)
    except:
        break