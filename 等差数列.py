while True:
    try:
        n=int(input())
        Sum=0
        item=2
        for i in range(n):
            Sum+=item
            item+=3
        print(Sum)
    except:
        break