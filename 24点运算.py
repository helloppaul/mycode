def dfs(arr,Sum,tmp,res):
    if Sum!=int(Sum):
        return 0
    if len(arr)==3 and tmp[0]!='+':
        return 0
    if arr==[]:
        if Sum==24:
            res.append(tmp)
            return 1
        else:
            return 0
    for i in range(len(arr)):
        if dfs(arr[:i]+arr[i+1:],Sum+M[arr[i]],tmp+'+'+arr[i],res) or dfs(arr[:i]+arr[i+1:],Sum-M[arr[i]],tmp+'-'+arr[i],res) or dfs(arr[:i]+arr[i+1:],Sum*M[arr[i]],tmp+'*'+arr[i],res) or dfs(arr[:i]+arr[i+1:],Sum/M[arr[i]],tmp+'/'+arr[i],res):
            return res[0]
    return 0

while True:
    try:
        arr=input().split(' ')
        M={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
        flag=1
        for v in arr:
            if v not in M:
                print('ERROR')
                flag=0
                break
        if flag==0:
            continue
        t=dfs(arr,0,'',[])
        print('NONE') if not t else print(t[1:])
    except:
        break