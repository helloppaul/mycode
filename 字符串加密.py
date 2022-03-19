'''
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保留第1个，将所得结果作为新字母表开头，并将新建立的字母表中未出现的字母按照正常字母表顺序加入新字母表。如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

T R A I L B Z E S C D F G H J K M N O P Q U V W X Y (实际需建立小写字母的字母表，此字母表仅为方便演示）

上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。因此，使用这个密匙， Attack AT DAWN (黎明时攻击)就会被加密为Tpptad TP ITVH。

请实现下述接口，通过指定的密匙和明文得到密文。

TRAILBLAZERS
输入：
nihao
ni
输出：
le
'''


while True:
    try:
        list_c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#                            初始字母表
        list_b=list(input())#     关键字
        list_d=sorted(set(list_b),key=list_b.index)#     关键字剔除重复项
        list_out1=list(input())#      需被翻译项
        list_out2=''#                 翻译结果
        for i in range(len(list_c)):
            if list_c[i] not in list_d:
                list_d+=list_c[i]                   #制作密码本
        for i in range(len(list_out1)):
            for j in range(len(list_c)):
                if list_c[j] in list_out1[i]:
                    list_out2+=list_d[j]#               嵌套循环加密加密
        print(list_out2)#                         输出结果
    except:
        break


'''import copy
def distct(lst_):
    lst=copy.deepcopy(lst_)
    Map={}
    for i,v in enumerate(lst):
        if v not in Map:
            Map[v]=1
        else:
            del lst[i]
    return lst


while True:
    try:
        encryplst_=list(input())
        slst=list(input())
        encryplst=distct(encryplst_)
        bigM={}
        smallM={}
        Lencryplst=len(encryplst)
        cnt=1
        for i in range(65,90):
            letter=chr(i)
            if cnt<= Lencryplst:
                bigM[letter]=encryplst[cnt-1].upper()
                smallM[letter.lower()]= encryplst[cnt-1].lower()
            else:
                bigM[letter] =letter
                smallM[letter.lower()]=letter.lower()
            cnt+=1
        print(bigM)
        print(smallM)
        res=''
        for v in slst:
            if v in bigM:
                res += bigM[v]
            else:
                res += smallM[v]
        print(res)
    except:
        break'''