# n, m = map(int,input().split())
# primary, annex = {}, {}
# for i in range(1,m+1):
#     x, y, z = map(int, input().split())
#     if z==0:#主件
#         primary[i] = [x, y]
#     else:#附件
#         if z in annex:#第二个附件
#             annex[z].append([x, y])
#         else:#第一个附件
#             annex[z] = [[x,y]]
# m = len(primary)#主件个数转化为物品个数
# dp = [[0]*(n+1) for _ in range(m+1)]
# w, v= [[]], [[]]
# for key in primary:
#     w_temp, v_temp = [], []
#     w_temp.append(primary[key][0])#1、主件
#     v_temp.append(primary[key][0]*primary[key][1])
#     if key in annex:#存在主件
#         w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
#         v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
#         if len(annex[key])>1:#存在两主件
#             w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
#             v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
#             w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
#             v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
#     w.append(w_temp)
#     v.append(v_temp)
# for i in range(1,m+1):
#     for j in range(10,n+1,10):#物品的价格是10的整数倍
#         max_i = dp[i-1][j]
#         for k in range(len(w[i])):
#             if j-w[i][k]>=0:
#                 max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
#         dp[i][j] = max_i
# print(dp[m][n])




# import itertools
# list1 = [1,2]
# list2 = []
# for i in range(1,len(list1)+1,1):
#     iter = itertools.combinations(list1,i)
#     #list2.append(list(iter))
#     list2=list2+list(iter)
#
# print(list2[0][0])
#list2.append(list(iter))
# print(len(list2[0]))
# for i in range(1,len(list1)+1):
#     iter = itertools.permutations(list1,i)
#     list2.append(list(iter))
# print(list2)



# 'Mabc'
# import itertools
# SubL=5
# a=[str(i) for i in range(SubL)]
# c=''.join(a)
# for i in itertools.combinations(c, 3):
#     print(''.join(i),end=" ")
# print('\n')

# n=input()
# print(n[::-1])

# arr=input().split(' ')
# print(' '.join(arr[::-1]))


# m1 = input().split(".")    #子网掩码
# m2 =""
# for i in m1:
#     temp = "{0:b}".format(int(i))   #二进制转换
#     m2 += '0'*(8-len(temp)) + temp  #补全8bit
# print(m2)

# while True:
#     try:
#         n=int(input())  #空瓶数量
#         if n==0:
#             break
#         AllGet=0
#         while n>0:
#             left=n % 3   #换后手中还剩下的空瓶数量
#             get=int((n-left)/3) #换到的汽水数量
#             AllGet+=get
#             n=left+get  #目前空瓶数量
#             if n<3:
#                 if n+1==3:
#                     AllGet += 1
#                 break
#         print(AllGet)
#     except:
#         break

# while True:
#     try:
#         s=input()
#         keydict={}
#         for m in s:
#             if m in keydict:
#                 keydict[m]+=1
#                 continue
#             keydict[m]=1
#         keydict=dict(sorted(keydict.items(),key=lambda kv:(kv[1],kv[0]),reverse=False))
#         minvalue=9999
#         for index in keydict:
#             if keydict[index]>minvalue:
#                 break
#             minvalue=keydict[index]
#             s=s.replace(index,'')
#         print(s)
#     except:
#         break

str='73'
print()
if str[::-1]=='7':
    print(1)
else: print(0)
