'''
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

1 3 6 10
2 5 9
4 8
7
'''
while True:
    try:
        n=int(input())
        b=1
        for i in range(n):
            b+=i
            s=''
            total=b
            for j in range(0,n-i):
                s += str(total) + ' '
                total+=(j+i+2)
            print(s)
    except:
        break