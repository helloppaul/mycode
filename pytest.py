a=[(1,0),(1,1)]
print(a[:])

# M={'a': 't', 'b': 'r', 'c': 'a', 'd': 'i', 'e': 'l', 'f': 'b', 'g': 'a', 'h': 'z', 'i': 'e', 'j': 's', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y'}
# print(M['A'])
# b=[0,1]+1
#
# print(b)



a=list(map(int,input().split(' ')))
print(a)

M={}
for i in range(0,10):
    M[str(i)]=1
print(M)

lst=[]
lst1=[]
M={}
M1={}
for i in range(65,91):
    M[chr(i)]=1
    M1[chr(i).lower()]=1
    lst.append(chr(i))
    lst1.append(chr(i).lower())
print(M)
print(M1)
print(lst)
print(lst1)

print(ord('a')-ord('A'))
print(ord('Z'))
num=167969729
print(bin(num)[2:])
a='{:0>10d}'.format(num)
print(a)
print()
s= (bin(int('a',16))[2:]).zfill(4)
print(s)
s=s[::-1]

s=hex(int(s, 2))[2:]
print(s)

# print(ord('F'))