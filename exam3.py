'''
5 10 20 50 85 1
6 1 2 3
输出
12
'''
while True:
    try:
        flag=1
        List = list(map(int, input().split(' ')))
        zhan = []
        index = -1
        Sum = 0
        for v in List:
            if index > 0 and flag==1:
                for y in range(index,-1,-1):
                    Sum=sum(zhan[y:index+1])   #index=1, zhan[1:2]
                    if v==Sum:  #出栈  从 y到 index出栈
                        if flag==0:
                            del zhan[y:]
                        else:
                            del zhan[y:index+1]
                        m=v*2
                        zhan.append(m)
                        v=m
                        index=len(zhan)-2
                        flag=0
            if flag==0:
                flag=1
                continue
            zhan.append(v)
            index += 1
        zhan=list(map(str,zhan))
        print(' '.join(zhan[::-1]))
    except:
        break