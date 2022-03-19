while True:
    try:
        n=int(input())
        arr=list(map(int,input().split(' ')[:n]))
        cnt=0
        Sum=0
        k=0
        for i in range(len(arr)):
            if arr[i]<0:
                cnt+=1
            elif arr[i]==0:
                continue
            else:
                Sum+=arr[i]
                k+=1
        print(cnt,format(Sum/k,'.1f'))
    except:
        break