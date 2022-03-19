

def dfs(arr,tmp,res):
    if arr==[]:
        res.append(tmp.copy())
        return 1
    for i in range(len(arr)):
        dfs(arr[:i]+arr[i+1:],tmp+[arr[i]],res)
    return res



nums=[1,2,3]
print(dfs(nums,[],[]))
