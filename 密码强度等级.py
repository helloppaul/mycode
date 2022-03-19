'''
38$@NoNoNo
~
VERY_SECURE
'''
while True:
    try:
        s=input()
        cnt=0
        sctype=[]
        score=0 #总分
        sc2={} #字母类型得分
        sc3=[] #数字得分
        sc4=[] #符号得分
        for v in s:
            if 65<=ord(v)<=90:
                sc2['大写']=1
            elif 97 <= ord(v) <= 122:
                sc2['小写'] = 1
            elif 48 <= ord(v) <= 57:
                sc3.append(v)
            elif 0x21 <= ord(v) <= 0x2F or 0x3A <= ord(v) <= 0x40 or 0x5B <= ord(v) <= 0x60 or 0x7B <= ord(v) <= 0x7E:
                sc4.append(v)
            cnt+=1
        #密码长度
        if cnt<=4:
            score+=5
        elif cnt>=5 and cnt<=7:
            score+=10
        elif cnt>=8:
            score += 25
        #字母种类
        if len(sc2)==1:
            score+=10
            sctype.append(1)
        elif len(sc2)>1:
            score += 20
            sctype.append(3)
        #数字
        if len(sc3)==1:
            score += 10
            sctype.append(1)
        elif len(sc3)>1:
            score += 20
            sctype.append(1)
        #符号
        if len(sc4)==1:
            score += 10
            sctype.append(1)
        elif len(sc4) > 1:
            score += 25
            sctype.append(1)
        score+=sum(sctype)

        #分数->评级
        if score>=90:
            print('VERY_SECURE')
        elif score>=80:
            print('SECURE')
        elif score>=70:
            print('VERY_STRONG')
        elif score >= 60:
            print('STRONG')
        elif score >= 50:
            print('AVERAGE')
        elif score >= 25:
            print('WEAK')
        elif score >= 0:
            print('VERY_WEAK')
    except:
        break