while True:
    try:
        s = input()
        k = int(input())
        AscList = {}
        slen=len(s)

        for i in range(slen):
            if s[i] not in AscList:
                AscList[s[i]]=[ord(s[i])]
            else:
                AscList[s[i]].append(ord(s[i]))
        AscList = sorted(AscList.items(),key=lambda kv:(kv[1],kv[0]) ,reverse=False)
        #letter=AscList[k-1]     # 第k个索引
        if k > slen:
            letter=AscList[-1][0]
        else:
            count=k
            for v in AscList:
                count-=len(v[1])
                if count==0:
                    letter=v[0]
        for i in range(slen):
            if s[i]==letter:
                print(i)
                break
    except:
        break