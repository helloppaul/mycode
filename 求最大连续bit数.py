while True:
    try:
        s=bin(int(input()))[2:]
        cnt=0
        Max=0
        for v in s:
            if v!='1':
                if cnt>Max:
                    Max=cnt
                cnt=0
                continue
            cnt+=1
        if cnt>Max:
            Max=cnt
        print(Max)
    except:
        break