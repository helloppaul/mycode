'''描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形
说明：
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等
请注意处理多组输入输出！

备注：
1<=N<=3000
输入描述：
有多组用例，每组都包含两行数据，第一行是同学的总数N，第二行是N位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列
输入：
8
186 186 150 200 160 130 197 200

输出：
4
说明：
由于不允许改变队列元素的先后顺序，所以最终剩下的队列应该为186 200 160 130或150 200 160 130     '''
def leftmax(List,l): #计算每个人左边的最大人数
    #l=len(list)
    dp=[1]*l
    for i in range(l):
        for j in range(i):
            if List[i]>List[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
    return dp
while True:
    try:
        N = int(input())
        List=list(map(int,input().split(' ')))
        dp_l=leftmax(List,N)    #计算每个人左边的最大人数
        dp_r=leftmax(List[::-1],N)[::-1]   #计算每个人右边的最大人数
        dp=[m+v for m,v in zip(dp_l,dp_r)]
        print(N-max(dp)+1)
    except:
        break