'''
案例1：
dec fab
——————————
5D37BF

案例2：
ab CD
——————————
3B5D
'''
while True:
    try:
        s=input().split(' ')
        slst=[]
        for p in s:
            for v in p:
                slst.append(v)
        even=[]  #奇数
        odd=[]   #偶数
        k=0
        for v in slst:
            if k%2==0:
                odd.append(v)
            else:
                even.append(v)
            k+=1

        odd=list(sorted(odd))
        even=list(sorted(even))
        for i in range(len(slst)):
            noupper = 0
            if i%2==0:
                m=odd[int(i/2)]
            else:
                m=even[int(i/2)]
            try:
                tmp = (bin(int(m, 16))[2:]).zfill(4)
                m_ = hex(int(tmp[::-1], 2))[2:]
            except:
                noupper=1
                m_=m
            slst[i] = m_
            try :
                if noupper==0:
                    slst[i]=m_.upper()
            except:
                slst[i] = m_
        print(''.join(slst))
    except:
        break