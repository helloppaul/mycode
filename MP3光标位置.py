'''每页仅显示4首歌曲
案例1：
10
UUUU
----------
7 8 9 10
7
案例2：
83
UUDUDDDDUDUUDDDDUDD
----------------------
3 4 5 6
6
案例3：
81
DDUUUDUUDDUDUUUUDUDDDDDUDUUDDUUDUDDUUUDUUUUUDDDDUDDDUUUDUUUDDDDDUDDDDDUDDDDDUDDUDDDDU
10 11 12 13
12
'''
while True:
    try:
        n=int(input()) #歌曲数量
        s=input() #操作命令符
        songs=[str(i) for i in range(1,n+1)]
        cur=0
        rcur=cur  #相对位置
        for v in s:
            if v=='U':
                rcur-=1
                if rcur < 0:
                    rcur=0
                cur-=1
                if cur <0:
                    cur = n - 1
                    rcur=3
            elif v=='D':
                rcur+=1
                if rcur>3:
                    rcur=3
                cur+=1
                if cur > n-1:
                    cur = 0
                    rcur=0
        print(' '.join(songs[cur-rcur:cur+(3-rcur)+1]))
        print(songs[cur])
    except:
        break