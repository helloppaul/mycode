while True:
    try:
        s1=input() #待加密
        s2=input() #待解密
        r1=''
        r2=''
        '''加密过程'''
        for i in s1:
            ord_=ord(i)
            if 65<= ord_<= 90 :
                ord_+=1
                if ord_== 91 :
                    ord_=65
                ord_+=32
                r1+= chr(ord_)
            elif 97 <=ord_<= 122 :
                ord_ += 1
                if ord_ == 123 :
                    ord_=97
                ord_ -= 32
                r1 += chr(ord_)
            elif 48 <=ord_<= 57 :
                ord_+=1
                if ord_== 58 :
                    ord_=48
                r1 += chr(ord_)
        '''解密过程'''
        for j in s2:
            ord_ = ord(j)
            if 65 <= ord_ <= 90 :   #大写
                ord_ -= 1
                if ord_ == 64 :
                    ord_=90
                ord_ += 32
                r2 += chr(ord_)
            elif 97 <= ord_ <= 122 :  #小写
                ord_ -= 1
                if ord_ == 96:
                    ord_ = 122
                ord_ -= 32
                r2 += chr(ord_)
            elif 48 <= ord_ <= 57 :
                ord_ -= 1
                if ord_ == 47 :
                    ord_ = 57
                r2 += chr(ord_)
        print(r1)
        print(r2)
    except:
        break