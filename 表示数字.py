while True:
    try:
        s=input()
        M={'0','1','2','3','4','5','6','7','8','9'}
        res=''
        flag=0
        for v in s:
            if v in M:
                if flag==0:
                    res+=('*'+v)
                    flag = 1
                else:
                    res+=v
                continue
            if flag==1:
                res+='*'
                flag=0
            res+=v
        if flag==1:
            res+='*'
        print(res)
    except:
        break