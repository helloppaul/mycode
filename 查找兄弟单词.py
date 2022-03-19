'''
定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如：ab和ba是兄弟单词。ab和ab则不是兄弟单词。
现在给定你n个单词，另外再给你一个单词str，让你寻找str的兄弟单词里，按字典序排列后的第k个单词是什么？
注意：字典中可能有重复单词。本题含有多组输入数据。

输入描述：
先输入单词的个数n，再输入n个单词。 再输入一个单词，为待查找的单词x 最后输入数字k

输出描述：
输出查找到x的兄弟单词的个数m 然后输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
输入：
3 abc bca cab abc 1
输出：
2
bca
'''
while True:
    try:
        s=input().split(' ')
        n=int(s[0])  #被查找的单词个数
        lst = s[1:n+1]
        k=int(s[n+2])    #需输出的兄弟单词的下标
        brolst=[]
        str_=s[n+1]
        lstr_=len(str_)
        maps={}
        for i in str_:
            if i in maps:
                maps[i]+=1
                continue
            maps[i]=1
        maps2=maps.copy()
        brocnt=0
        for v in lst:
            if len(v)==lstr_ and v!=str_:
                flag=1
                for m in v:
                    if m not in maps:  #不是兄弟单词
                        flag=0
                        break
                    maps[m]-=1
                    if maps[m]<0:  #超出兄弟单词的字符
                        flag=0
                        break
                if flag==1: #and (v not in brolst):
                    brolst.append(v)
                    brocnt+=1
                maps.update(maps2)
        brolst=sorted(brolst)
        #print(brolst)
        print(brocnt)
        if k<=brocnt:
            print(brolst[k-1])
    except:
        break