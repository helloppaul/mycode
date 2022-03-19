while True:
    try:
        s=input()
        n=int(input())
        ls=len(s)
        Max_cnt=0
        Max_substr=''
        for i in range(0,ls-n+1):
            vs=s[i:i+n]
            cnt_CG=0
            for v in vs:
                if v in ['C','G']:
                    cnt_CG+=1
            if cnt_CG>Max_cnt:
                Max_cnt=cnt_CG
                Max_substr = vs
        print(Max_substr)
    except:
        break