
def toBinary(n):
    s=''
    while int(n)>0:
        s+=str(n%2)
        n=int(n/2)
    ls=len(s)
    if ls<8:
        return '{:0>8s}'.format(s[::-1])
    elif 8<ls<16:
        return '{:0>16s}'.format(s[::-1])
    elif 16<ls<32:
        return '{:0>32s}'.format(s[::-1])
    return format(s[::-1])

def toInt(s):
    k=1
    Sum=0
    for v in s[::-1]:
        Sum+=int(v)*2**(k-1)
        k+=1
    return Sum

while True:
    try:
        ipLst=input().split('.')
        ip10=toBinary(int(input()))
        sip=''
        for i,v in enumerate(ipLst):
            sip+=toBinary(int(v))
        sip1=''
        step=8
        for i in range(0,len(ip10),step):
            sip1+=('.'+str(toInt(ip10[i:i+step])))
        print(toInt(sip))
        print(sip1[1:])

    except:
        break



