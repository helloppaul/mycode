while True:
    try:
        ip=input().split('.')
        Sum=0
        for v in ip:
            Sum+=len(bin(int(v))[2:])
        if Sum>32:
            print('NO')
        else:
            print('YES')
    except:
        break