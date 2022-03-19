'''
输入：
15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123
5 6 3 6 3 0

24 7907 610 4359 55 812 3002 10706 2470 8332 8573 3840 8105 9213 10159 11882 6517 7357 6398 4586 215 3420 4927 7159 9414
10 85 122 46 55 110 47 77 119 50 58


4 2470 8332 8573 3840
5 47 77 119 50 58

输出：
30 3 6 0 123 3 453 7 3 9 453456 13 453 14 123 6 7 1 456 2 786 4 46 8 665 9 453456 11 456 12 786'''
def bsort(a):  #冒泡排序，从小到大(去重)
    a.append(-1)
    while True:
        i=0
        flag=0
        while a[i+1]!=-1:
            if a[i+1]<a[i]:
                tmp=a[i+1]
                a[i+1]=a[i]
                a[i]=tmp
                flag=1
            elif a[i+1]==a[i]:
                del a[i+1]
            i+=1
        if flag==0:
            break
    del a[-1]
    return a

while True:
    try:
        I = input().split(' ')
        if I[-1]=='':
            del I[-1]
        I=list(map(int,I))
        R=input().split(' ')
        if R[-1]=='':
            del R[-1]
        R = list(map(int,R))
        Nr=R[0]
        Ni=I[0]
        del R[0]
        del I[0]
        bsort(R)
        outstr=''
        total=0
        for v in R:
            vs=str(v)
            vsl=len(vs)
            cnt=0
            s=''
            for j in range(Ni):
                ms=str(I[j])
                for k in range(0,len(ms),1):
                    if vs==ms[k:k+vsl]:
                        s+=(' '+str(j)+' '+ms)
                        cnt+=1
                        break
            if cnt>0:
                total+=(cnt*2+2)
                outstr+=(' '+vs+' '+str(cnt)+s)
        print(str(total) + outstr)
    except:
        break