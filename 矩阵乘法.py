'''
2
3
2
1 2 3
3 2 1
1 2
2 1
3 3
~
14 13
10 11
'''
while True:
    try:
        x=int(input())
        y=int(input())
        z=int(input())
        A=[]
        B=[]
        M=[]
        for i in range(x):
            A.append(list(map(int,input().split(' '))))
            M.append([])
        for i in range(y):
            B.append(list(map(int,input().split(' '))))
        for i in range(x):
            for j in range(z):
                value=0
                for k in range(y):
                    value+=A[i][k]*B[k][j]
                M[i].append(value)
                print(M[i][j],end=' ')
            print()
    except:
        break