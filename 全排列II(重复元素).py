def dfs(arr,tmp,res):
    if not arr:
        res.append(tmp)
        return res
    M={}
    for i in range(len(arr)):
        if arr[i] not in M:
            M[arr[i]]=1
        else:
            continue
        dfs(arr[:i]+arr[i+1:], tmp+[arr[i]], res)
    return res

nums=[1,2,2]
print(dfs(nums,[],[]))


