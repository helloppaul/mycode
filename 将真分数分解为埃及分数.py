'''
a/b=1/(p+1)+(a-r)/(a*p+r)(1+p)
'''
while True:
    try:
        a,b = list(map(int,input().split('/')))
        l=[]  #用于存放埃及分数
        while True:
            if b%a==0:
                l.append(str(1)+'/'+str(int(b/a)))
                break
            c = b // a + 1
            l.append('1/' + str(c))
            a=a-b%a
            b = b * c
        print('+'.join(l))
    except:
        break
