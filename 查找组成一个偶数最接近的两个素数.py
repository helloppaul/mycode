def isprime(n):  #判断n是不是素数，素数只能被1和自己整除
    m=int(n**(1/2))+1
    for i in range(2,m,1):
        if n % i == 0:
            return 0
    return 1

while True:
    try:
        num=int(input())
        pairs=[]  #存放素数对
        if num==2:
            print(1)
            print(1)
        endflag=0
        for i in range(3,num):
            if not isprime(i):
                continue
            for j in range(i,num):
                if not isprime(j):
                    continue
                if i+j==num:
                    if i==j:
                        print(i)
                        print(j)
                        endflag=1
                        break
                    pairs.append([i,j,j-i])
                    break
            if endflag==1:
                break
        if endflag==1:
            continue
        min=pairs[0][2]
        outpairs=[]
        for v in pairs:
            if v[2]<min:
                min=v[2]
                outpairs=[v[0],v[1]]
        print(outpairs[0])
        print(outpairs[1])
    except:
        break