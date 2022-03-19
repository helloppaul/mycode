
# def reduceNum(n):
#     print ('{} = '.format(n), end=" ")
#     if not isinstance(n, int) or n <= 0 :
#         print ('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :
#         print ('{}'.format(n))
#     while n not in [1] : # 循环保证递归
#         for index in range(2, n + 1) :
#             if n % index == 0:
#                 n //= index # n 等于 n//index
#                 if n == 1:
#                     print (index )
#                 else : #
#                     print ('{} *'.format(index), end=" ")
#                 break
# n=int(input())
# reduceNum(n)

n= int(input())
for i in range(2,int(n**0.5)+1):
    while n % i ==0:
        print(i, end=" ")
        n//=i
if n!=1:
    print(n,end=" ")



