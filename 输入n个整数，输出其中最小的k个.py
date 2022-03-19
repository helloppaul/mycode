'''
输入：
5 2
1 3 5 7 2
输出：
1 2
'''
while True:
    try:
        n,k=input().split(' ')
        n=int(n)
        k=int(k)
        List=list(map(int,input().split(' ')))
        List=sorted(List,reverse=False)
        print(' '.join(list(map(str,List[:k]))))
    except:
        break