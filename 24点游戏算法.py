'''
案例1：
7 2 1 10
------------
true
案例2：
3 9 3 4
-------
true
案例3：
2 10 7 4
-------
true
'''
def dfs(i,snum):
    if i==len(nlst):
        if snum==24:
            return 1
        return 0
    if dfs(i+1,snum+nlst[i])==1:
        print("+")
        return 1
    if dfs(i+1,snum-nlst[i])==1:
        print("-")
        return 1
    if dfs(i+1,snum * nlst[i]) == 1:
        print("*")
        return 1
    if dfs(i+1,snum / nlst[i]) == 1:
        print("/")
        return 1
    return 0
while True:
    try:
        nlst=list(map(int,input().split(' ')))
        snum=0
        if dfs(0,snum)==1:
            print('true')
        else:
            print('false')
    except:
        break