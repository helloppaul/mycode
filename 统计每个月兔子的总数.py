'''描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？

本题有多组数据。

输入描述：
输入int型表示month

输出描述：
输出兔子总数int型

输入：
9

输出：
34
'''
while True:
    try:
        n_month=int(input())
        rblist=[0]  #兔子月份序列
        for i in range(0,n_month):
            # rblen=len(rblist)
            for j in range(len(rblist)):   #rblist[j]是每只兔子的年龄
                rblist[j]+=1
                if rblist[j]>=3:
                    rblist.append(1)
        print(len(rblist))
    except:
        break