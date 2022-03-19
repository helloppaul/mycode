n=float(input())
r_n=int(n)  #取整
r=n-int(n)  #余数
if r>=0.5:
    r_n+=1
    print(r_n)
else:
    print(r_n)


