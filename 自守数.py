'''
自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数
'''
while True:
    try:
        n=int(input())
        cnt=0
        for i in range(0,n+1):
            sn=str(i)
            lsn=len(sn)
            if str(i**2)[-lsn::]==sn:
                cnt+=1
        print(cnt)
    except:
        break