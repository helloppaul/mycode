'''
6 2 1 2 3 2 5 1 4 5 7 2 2
'''
while True:
    try:
        lst=list(map(int,input().split(' ')))
        ls = len(lst)
        n=lst[0]  #链表结点个数
        headv=lst[1]  #头结点值
        dvalue=lst[ls-1]  #待删除的结点
        link={headv:None}  #链表
        head=link #头结点
        for i in range(2,ls-2,2):
            cur=head #遍历的游标
            curv=list(cur.keys())[0]
            while True: #查找结点，将新节点插入查找到的结点后面
                if curv==lst[i+1]:
                    tmp = cur[curv]
                    cur[curv]={lst[i]:tmp}
                    break
                cur=cur[curv]    #游标移动到下一结点
                if cur is None :
                    break
                curv=list(cur.keys())[0]
        cur=head
        curv=headv
        #删除结点
        while True:
            if curv != dvalue:
                print(curv,end=' ')
            cur=cur[curv]
            if cur is None:
                break
            curv=list(cur.keys())[0]
    except:
        break
'''
5 2 3 2 4 3 5 2 1 4 3
'''