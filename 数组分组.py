def f(g5,g3,other):
    if not other:
        if abs(sum(g5)-sum(g3))==0:
            return True
        return 0

    if f(g5+[other[0]], g3,other[1:]) or f(g5 , g3+[other[0]],other[1:] ):
        return True
    return False
    # if arr==[]:
    #     if abs(sum(g5)-sum(g3))==0:
    #         return 1
    #     return 0
    # for i in range(len(arr)):
    #     if arr[i]%5==0:
    #         return f(arr[:i]+arr[i+1:],g5+[arr[i]],g3)
    #     elif arr[i]%3==0:
    #         return f(arr[:i]+arr[i+1:],g5,g3+[arr[i]])
    #     else:
    #         if f(arr[:i]+arr[i+1:], g5+[arr[i]], g3) or f(arr[:i] + arr[i + 1:], g5 , g3+[arr[i]]):
    #             return True
    # return False
'''
4
1 5 -5 1
~
13
3 0 1 3 -2 -1 4 -2 -1 5 0 -2 -2 
'''
while True:
    try:
        n=int(input())
        arr=list(map(int,input().split(' ')[:n]))
        g5=[]
        g3=[]
        other=[]
        for v in arr:
            if v%5==0:
                g5.append(v)
            elif v%3==0:
                g3.append(v)
            else:
                other.append(v)
        print('true') if f(g5,g3,other) else print('false')
    except:
        break