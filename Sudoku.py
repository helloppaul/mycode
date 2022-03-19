'''
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1

5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1
'''
def isEqual(sMatrix,x,y):
    #和同列的相比有没有相同，若有，则返回False
    for i in range(9):
        if sMatrix[i][y] == sMatrix[x][y] and i!=x:
            return False
    #和同行的相比有没有相同，若有，则返回False
    for j in range(9):
        if sMatrix[x][j] == sMatrix[x][y] and j!=y:
            return False
    #9宫格内的相比，若有相同，则返回False
    m,n= (x-x%3),(y-y%3)
    for i in range(m,m+3):
        for j in range(n,n+3):
            if sMatrix[i][j] == sMatrix[x][y] and x!=i and y!=j:
                return False
    return True
def dfs(sMatrix):
    for i in range(9):
        for j in range(9):
            if sMatrix[i][j] == 0:
                for k in range(1, 10):
                    sMatrix[i][j] = k
                    if isEqual(sMatrix, i, j):
                        if dfs(sMatrix):
                            return True
                    sMatrix[i][j] = 0
                return False  #说明上一状态的数字不合理
    #完成所有的遍历
    return True
while True:
    try:
        sMatrix=[]
        for i in range(9):
            sMatrix.append(list(map(int,input().split(' '))))
        dfs(sMatrix)
        for v in sMatrix:
            print(' '.join(list(map(str,v))))
    except:
        break
'''
输入
0 9 5 0 2 0 0 6 0
0 0 7 1 0 3 9 0 2
6 0 0 0 0 5 3 0 4
0 4 0 0 1 0 6 0 7
5 0 0 2 0 7 0 0 9
7 0 3 0 9 0 0 2 0
0 0 9 8 0 0 0 0 6
8 0 6 3 0 2 1 0 5
0 5 0 0 7 0 2 8 3
输出
3 9 5 7 2 4 8 6 1
4 8 7 1 6 3 9 5 2
6 2 1 9 8 5 3 7 4
9 4 2 5 1 8 6 3 7
5 6 8 2 3 7 4 1 9
7 1 3 4 9 6 5 2 8
2 3 9 8 5 1 7 4 6
8 7 6 3 4 2 1 9 5
1 5 4 6 7 9 2 8 3
'''