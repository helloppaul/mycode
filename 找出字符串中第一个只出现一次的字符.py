'''
asdfasdfo
aabb
----------
o
-1
'''
while True:
    try:
        s=input()
        ls=len(s)
        M=set()
        finded=0
        for i in range(ls):
            v=s[i]
            flag = 0
            for k in range(ls):
                if i==k:
                    continue
                if v==s[k]:
                    flag=1
                    break
            if k==ls-1 and flag==0:  #正常结束，并且最后一个和最后一个字符也不相等
                print(v)
                finded=1
                break
        if finded==0:
            print(-1)
    except:
        break