'''
6
2 5 1 5 4 5
~
30
186 13 322 264 328 110 120 73 20 35 240 97 150 221 284 324 46 219 239 284 128 251 298 319 304 36 144 236 163 122
'''
def dfs(arr,head,tmp,res,k):
    if not arr:
        res.append(tmp)
        return 1
    if head>=arr[0]:
        return 0
    else:
        tmp+=[arr[0]]

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if dfs(arr[j+1:], arr[i], tmp , res,k+1)==1:
                if k==1:
                    break
                tmp.pop()
                return  res #回溯
    return res


        # res.append(len(tmp))
        # return max(res)


while True:
    try:
        n=int(input())
        arr=list(map(int,input().split(' ')[:n]))
        out=[]
        print(dfs(arr,-1,[],[],0))
    except:
        break