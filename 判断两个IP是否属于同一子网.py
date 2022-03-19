'''子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
子网掩码与IP地址结构相同，是32位二进制数，其中网络号部分全为“1”和主机号部分全为“0”。利用子网掩码可以判断两台主机是否中同一子网中。若两台主机的IP地址分别与它们的子网掩码相“与”后的结果相同，则说明这两台主机在同一子网中。
示例：
I P 地址　 192.168.0.1
子网掩码　 255.255.255.0

转化为二进制进行运算：

I P 地址　  11000000.10101000.00000000.00000001
子网掩码　11111111.11111111.11111111.00000000

AND运算   11000000.10101000.00000000.00000000

转化为十进制后为：
192.168.0.0

I P 地址　 192.168.0.254
子网掩码　 255.255.255.0

转化为二进制进行运算：

I P 地址　11000000.10101000.00000000.11111110
子网掩码  11111111.11111111.11111111.00000000

AND运算  11000000.10101000.00000000.00000000

转化为十进制后为：
192.168.0.0

通过以上对两台计算机IP地址与子网掩码的AND运算后，我们可以看到它运算结果是一样的。均为192.168.0.0，所以这二台计算机可视为是同一子网络。

输入一个子网掩码以及两个ip地址，判断这两个ip地址是否是一个子网络。
若IP地址或子网掩码格式非法则输出1，若IP1与IP2属于同一子网络输出0，若IP1与IP2不属于同一子网络输出2。

注:
有效掩码与IP的性质为：
1. 掩码与IP每一段在 0 - 255 之间
2. 掩码的二进制字符串前缀为网络号，都由‘1’组成；后缀为主机号，都由'0'组成

255.255.255.0
192.168.224.256
192.168.10.4
255.0.0.0
193.194.202.15
232.43.7.59
255.255.255.0
192.168.0.254
192.168.0.1

1
2
0
'''
while True:
    try:
        netmask=input().split('.')
        ip1=input().split('.')
        ip2=input().split('.')
        flag=0
        for i in range(4):
            if not (0<=int(netmask[i])<=255 and 0<=int(ip1[i])<=255 and 0<=int(ip2[i])<=255):
                print(1)
                flag=1
                break

            try:
                if int(netmask[i])<255 and int(netmask[i+1]) != 0:
                    print(1)
                    flag = 1
                    break
            except:
                pass

            #转二级制
            ans1=int(netmask[i])&int(ip1[i])
            ans2=int(netmask[i])&int(ip2[i])
            if ans1!=ans2:
                print(2)
                flag=1
                break
        if flag==0:
            print(0)
    except:
        break