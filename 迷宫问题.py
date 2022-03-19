'''输入描述：
输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
输出描述：
左上角到右下角的最短路径，格式如样例所示。
输入：
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出：
(0,0)
(1,0)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
(3,4)
(4,4)

4 6
0 0 1 1 1 1
1 0 1 0 0 0
1 0 0 0 1 0
1 1 1 1 0 0

5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
0 1 1 1 0
0 0 0 1 0
'''
def goNext(i,j,signal):
    if i == 0 and j == 0:
        print('(' + str(i) + ',' + str(j) + ')')
        return 1
    if Matrix[i][j]=='1':
        return 0

    if j>0 and signal!='right':
        r1 = goNext(i, j - 1,'left')  # 向左
        if r1 :
            print('(' + str(i) + ',' + str(j) + ')')
            return 1
    if i>0 and signal!='down':
        r2 = goNext(i - 1, j,'up')  # 向上
        if r2 :
            print('(' + str(i) + ',' + str(j) + ')')
            return 1

    if j<Max[1]-1 and signal!='left':
        r3 = goNext(i, j + 1,'right')    # 向右
        if r3 :
            print('(' + str(i) + ',' + str(j) + ')')
            return 1

    if i<Max[0]-1 and signal!='up':
        r4 = goNext(i + 1, j,'down')   # 向下
        if r4 :
            print('(' + str(i) + ',' + str(j) + ')')
            return 1
    return 0

while True:
    try:
        n,m=list(map(int,input().split(' ')))
        Max=[n,m]
        Matrix=[]

        for i in range(n):
            Matrix.append(input().split(' ')[:m])
        goNext(n-1,m-1,'')
    except:
        break