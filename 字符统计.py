while True:
    try:
        s=input()
        cntM={}

        for v in s:
            if v not in cntM:
                cntM[v]=1
            else:
                cntM[v]+=1
        ans=''
        for item in sorted(cntM.items(),key=lambda kv:(-kv[1],kv[0])):
            ans+= item[0]
        print(ans)
    except:
        break