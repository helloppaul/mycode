while True:
    try:
        n=float(input())
        print(float('%.1f' % n**(1/3)))
    except:
        break