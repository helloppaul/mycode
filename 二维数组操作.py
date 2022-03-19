while True:
    try:
        m,n=map(int,input().split(' '))
        x1,y1,x2,y2=map(int,input().split(' '))
        row=int(input())
        col=int(input())
        x,y=map(int,input().split(' '))

        if m>9 or n>9:
            print(-1)
        else:
            arr=[[0]*n for i in range(m)]
            print(0)

        try:
            arr[x1][y1],arr[x2][y2]=arr[x2][y2],arr[x1][y1]
            print(0)
        except:
            print(-1)

        if m+1>9 or row>m-1:
            print(-1)
        else:
            print(0)
        if n+1>9 or col>n-1:
            print(-1)
        else:
            print(0)
        try:
            a=arr[x][y]
            print(0)
        except:
            print(-1)
    except:
        break