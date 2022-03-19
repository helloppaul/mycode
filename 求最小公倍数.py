while True:
    try:
        a,b=map(int,input().split(' '))
        if a>b:
            a,b=b,a
        for i in range(1,a+1):
            if (b*i)%a==0:
                print(b*i)
                break
    except:
        break