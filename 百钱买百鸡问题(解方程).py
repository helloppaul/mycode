'''百钱买鸡问题
鸡翁 每只5元
鸡母 每只3元
鸡仔 3只1元，一只 1/3元
问：花100元买100只鸡有多少种买法
'''
while True:
    try:
        n=input()
        for x in range(21):
            y=(100-7*x)/4
            z=100-x-y
            if y==int(y) and  y>=0 and z>=0:
                print(x,int(y),int(z))
    except:
        break