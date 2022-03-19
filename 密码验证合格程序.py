'''描述
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有相同长度大于2的子串重复

输入描述：
一组或多组长度超过2的字符串。每组占一行

输出描述：
如果符合要求输出：OK，否则输出NG

输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

))20Uq%0
复制
输出：
OK
NG
NG
OK
'''
def is_sub(index,sub,str):
    if sub in str[index+1:]:
        return True
    return False

while True:
    try:
        s=input()
        i=0  #字符串长度
        b=[0,0,0,0]    #字符串种类数量
        flag=False   #是否存在子串
        sub=''
        for v in s:
            sub+=v
            if v.isdigit():
                b[0]=1
            elif 65<=ord(v)<=90:  #大写字母
                b[1]=1
            elif 97<=ord(v)<=122:
                b[2]=1
            else:
                b[3] = 1
            if i>1:
                flag=is_sub(i,sub[i-2:], s)
                if flag==True:
                    break
            i+=1
        if flag==True:
            print('NG')

            continue
        if i<=8:
            print('NG')
            continue
        if sum(b)<3:
            print('NG')
            continue

        print('OK')
    except:
        break
