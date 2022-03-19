while True:
    try:
        n=int(input())   #候选人数
        names=input().split(' ')[:n]
        Mnames={v:0 for v in names}
        Mnames['Invalid']=0
        m=int(input())   #投票人数
        votes=input().split(' ')[:m]
        for v in votes:
            if v in Mnames:
                Mnames[v]+=1
            else:
                Mnames['Invalid']+=1
        for idx in Mnames:
            print(idx+' : '+str(Mnames[idx]))
    except:
        break