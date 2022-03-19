'''
输入：
4
0 1
0 2
1 2
3 4
'''
n=int(input())
key={}
for i in range(n):
    k,v=map(int,input().split(' '))
    if k in key:
        key[k]+=v
    else:
        key[k]=v
for j in sorted(key):
    print("{} {}".format(j, key[j]))