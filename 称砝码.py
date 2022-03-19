'''描述
现有一组砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
注：
称重重量包括 0

本题有多组输入
数据范围：每组输入数据满足  ，  ，
输入描述：
输入包含多组测试数据。
对于每组测试数据：
第一行：n --- 砝码数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
输出描述：
利用给定的砝码可以称出的不同的重量数
输入：
2
1 2
2 1
10
4 185 35 191 26 148 149 3 172 147
3 5 2 1 5 5 3 1 4 2
输出：
5
3375
'''
while True:
    try:
        n=int(input())
        mlst=list(map(int,input().split(' ')[0:n]))
        numlst=list(map(int,input().split(' ')[0:n]))
        res=[0]
        for i in range(n):
            for j in range(1,numlst[i]+1):
                temp=set(res)
                for v in temp:
                    res.append(v+mlst[i])
        print(len(set(res)))
    except:
        break