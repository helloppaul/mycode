from fractions import Fraction as fc

while True:
    try:
        target=fc(input())
        a=target.numerator #分子
        b=target.denominator  #分母
        l=[]
        n=2
        while target.numerator!=1:
            if target>fc(1,n):
                l.append(str(n))
                target-=fc(1,n)
            if n>=b:
                n+=b
            else:
                n+=1
        l.append(str(target.denominator))
        print('1/'+'+1/'.join(l))
    except:
        break
