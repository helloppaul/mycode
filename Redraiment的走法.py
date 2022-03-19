'''
6
2 5 1 5 4 5
~
30
186 13 322 264 328 110 120 73 20 35 240 97 150 221 284 324 46 219 239 284 128 251 298 319 304 36 144 236 163 122
'''
def dfs(arr,head,jump,tmp,res):
    # if len(arr)==1:
    #     if jump<=head:
    #         tmp.pop()
    #     res.append(tmp)
    #     return 1
    if jump<=head:
        return 0

    # for i in range(len(arr)):
    for j in range(1,len(arr)):
        dfs(arr[j:], arr[0],arr[j], tmp + [arr[j]], res)
    res.append(len(tmp))
    return max(res)


while True:
    try:
        n=int(input())
        arr=list(map(int,input().split(' ')[:n]))
        out=[]
        for i in range(len(arr)):
            out.append(dfs(arr[i:],-1,0,[arr[i]],[]))
        print(max(out))
    except:
        break