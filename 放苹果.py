'''
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
输入描述：
输入两个int整数
输出描述：
输出结果，int型
输入：
7 3
输出：
8
'''

def dfs(plateNo,apples,leftapples):
    # plates.append(apples)
    # leftapples = cond[0] - sum(plates)  # 剩余苹果数量

    if plateNo<=cond[1]-1:
        i=plateNo
        for j in range(leftapples+1):  #cond[0]-apples 表示 剩余苹果数量
            if not dfs(i+1,j,leftapples-j):
                continue
            plates.append(j)


            # if dfs(i+1, j):
            #     plates.append(j)
            #     return 1
    #n个盘子放完
    if sum(plates)!=cond[0]:
        return 0
    return 1


while True:
    try:
        m,n=list(map(int,input().split(' ')))
        cond=[m,n]  #m苹果数量；n盘子数量
        platesConb=[]
        plates = []
        for j in range(m):  #所有可能性
            dfs(0,j,m)
            platesConb.append(plates)
            plates=[]
        print(platesConb)
    except:
        break