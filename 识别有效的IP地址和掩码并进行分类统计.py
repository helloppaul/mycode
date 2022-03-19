'''描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
输入：
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0



输出：
1 0 1 0 0 2 1
'''
def isvalid(lists,snum,enum):
    for m in lists:
        if not snum<=int(m)<=enum:
            return False
    return True


A=0
B=0
C=0
D=0
E=0
Error=0
Pv=0  #私有IP地址数量
tmplist=[i for i in range(255)]
Privatelist={10:[tmplist]*3,172:[[i for i in range(16,31+1)],tmplist,tmplist],192:[[168],tmplist,tmplist] }
while True:
    try:
        main, sub = input().split('~')
        MainRow=main.split('.')
        SubRow=sub.split('.')
        MainRowL=len(MainRow)
        SubRowL=len(SubRow)
        a,b,c,d,e,err,pv=[0,0,0,0,0,0,0]
        #检查空位
        Err_=Error
        for j in range(MainRowL):
            if MainRow[j]=='':
                Error += 1
                break
        if Error>Err_:
            continue
        '''判断IP'''
        isPrivate=-1
        if int(MainRow[0]) in Privatelist:  #私有IP分类
            isPrivate = 1
            R0=int(MainRow[0])
            for j in range(1,2+1):
                if not int(MainRow[j]) in Privatelist[R0][j-1]:
                    isPrivate=0
                    break
            if isPrivate==1:
                pv+=1

        if 1<=int(MainRow[0])<=126 :  #A分类
            flag=isvalid(MainRow[1:], 0,255)
            if flag==False:
                Error+=1
                continue
            a+=1
        elif 128<=int(MainRow[0])<=191 :  #A分类
            flag=isvalid(MainRow[1:], 0,255)
            if flag==False:
                Error+=1
                continue
            b+=1
        elif 192<=int(MainRow[0])<=223 :  #C分类
            flag = isvalid(MainRow[1:], 0, 255)
            if flag==False:
                Error += 1
                continue
            c+=1
        elif 224<=int(MainRow[0])<=239 :  #D分类
            flag = isvalid(MainRow[1:], 0, 255)
            if flag==False:
                Error += 1
                continue
            d+=1
        elif 240 <= int(MainRow[0]) <= 255 :  #E分类
            flag = isvalid(MainRow[1:], 0, 255)
            if flag==False:
                Error += 1
                continue
            e+=1

        '''判断子网掩码'''
        SubStr = ''
        # 检查空位 以及 初始化 子网掩码
        for j in range(SubRowL):
            if SubRow[j]=='':
                Error += 1
                break
            temp=bin(int(SubRow[j],10))[2:]
            SubStr +='0'*(8-len(temp))+temp
        #判断是否为非法子网掩码
        if SubStr[0] == '0':
            Error+=1
            continue
        IsAllOne=1
        IsAllZero=1
        IsZeroShow=0
        Err_=Error
        #判断子网掩码每个元素是否满足条件
        for m in SubStr[1:]:
            if m=='1':
                IsAllZero=0
                if IsZeroShow==1:
                    Error+=1
                    break
            elif m=='0':
                IsAllOne=0
                IsZeroShow=1
        if Error>Err_:
            continue
        elif IsAllZero==1 or IsAllOne==1:
            Error+=1
            continue
        A+=a
        B+=b
        C+=c
        D+=d
        E+=e
        Pv+=pv
    except:
        break
print('{} {} {} {} {} {} {}'.format(A,B,C,D,E,Error,Pv))


'''他人写的
ans = [0]*7

while True:
    try:
        m = input().split("~")
        m0 = m[0].split(".")    #ip 地址
        m1 = m[1].split(".")    #子网掩码
        
        #检查是否有“空”的格式错误， 例如192..0.2
        flag = False
        for i in m0 + m1:
            if i.isdigit() == False:
                ans[5] += 1 # type 5
                flag = True
                break
        if flag == True:
            continue
        
        #求子网掩码的二进制格式 = m2
        m2 =""
        for i in m1:
            temp = "{0:b}".format(int(i))   #二进制转换
            m2 += '0'*(8-len(temp)) + temp  #补全8bit
        
        #检查子网掩码格式
        count = 0
        for i in range(len(m2)-1):
            if m2[i] != m2[i+1]:
                count += 1
        if count != 1:     #==1 说明格式正确
            ans[5] += 1 # type 5
            count = 0
            continue
        
        #统计
        if int(m0[0]) >= 1 and int(m0[0]) <= 126:
            ans[0] += 1
        elif int(m0[0]) >= 128 and int(m0[0]) <= 191:
            ans[1] += 1
        elif int(m0[0]) >= 192 and int(m0[0]) <= 223:
            ans[2] += 1
        elif int(m0[0]) >= 224 and int(m0[0]) <= 239:
            ans[3] += 1
        elif int(m0[0]) >= 240 and int(m0[0]) <= 255:
            ans[4] += 1
        
        if int(m0[0]) == 10:
            ans[6] += 1
        elif int(m0[0]) == 172 and int(m0[1]) >= 16 and int(m0[1]) <= 31:
            ans[6] += 1
        elif int(m0[0]) == 192 and int(m0[1]) == 168:
            ans[6] += 1
    except:
        break

for i in range(len(ans)-1):
    print(ans[i],end=" ")
print(ans[-1],end="")'''