
'''
4
2 5 6 13
'''
def is_prime(x):
    for i in range(2,int(x ** 0.5)+1):
        if x % i == 0 :
            return 0
    return 1

def match(i):
    for j in range(n):
        if array[i][j]==1 and not visted[j]:  #有边且未访问
            visted[j]=1
            if matched[j]==-1 or match(matched[j]):  #右侧元素没有对应左侧元素或右侧元素对应的左侧元素还有其他选择
                matched[j]=i
                return True
    return False

while True:
    try:
        '''1.将奇数和偶数分成两组'''
        n = int(input())
        lst=list(map(int,input().split(' ')))
        odds,evens=[],[]  #奇数，偶数
        for v in lst:
            if v % 2 == 0 :
                evens.append(v)
            else:
                odds.append(v)
        '''2.根据奇数分组和偶数分组，形成可匹配素数的邻接矩阵'''
        m=len(odds)  #奇数个数
        n=len(evens)  #偶数个数
        array=[[-1]*n for j in range(m) ]
        for i,x in enumerate(odds) :
            for j,y in enumerate(evens) :
                array[i][j]=is_prime(x+y)
        '''3.生成匹配矩阵和访问矩阵，开始匈牙利算法'''
        matched=[-1]*n    #右侧元素对应匹配的左侧元素
        counter=0
        for i in range(m):
            visted=[False] * n
            if match(i):
                counter += 1
        print(counter)
    except:
        break


