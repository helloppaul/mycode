def f(x,n):
    return x**3-n

while True:
    try:
        flag=0
        n=float(input())
        a=min(-1,n)
        b= max(1,n)
        while f(a,n)*f(b,n)>=0:
            a-=1
            b+=1
        eps=0.001
        c=(a+b)/2
        while abs(a-b)>eps:
            if f(c,n)*f(b,n)<0:
                a=c
            elif f(c,n)*f(a,n)<0:
                b=c
            c=(a+b)/2
        print(float('%.1f' % c))
    except:
        break