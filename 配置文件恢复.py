'''
reset board
'''
while True:
    try:
        sc=input().strip().split()   #命令
        scM={#'reset':'reset what',
             'reset board':'board fault',
             'board add':'where to add',
             'board delete':'no board at all',
             'reboot backplane':'impossible',
             'backplane abort':'install first',
             'he he':'unknown command'}
        lsc=len(sc)
        if lsc>2 or lsc<1:
            print('unknown command')
            break
        if lsc==1 :
            one = 'reset'
            if sc[0] == one[:len(sc[0])]:
                print('reset what')
                continue
            print('unknown command')
            continue
        index=[]
        for idx in scM:
            keys=idx.split(' ')
            flag = 1
            for i in range(lsc):
                tsc=sc[i]
                if tsc!=keys[i][:len(tsc)]:
                    flag=0
                    break
            if flag==1:
                index.append(idx)
        if len(index)>1:
            print('unknown command')
        else:
            print(scM[index[0]])
    except:
        break