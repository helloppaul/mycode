class Node():
    def __init__(self,id='0',val=None,next=[]):
        self.id=id
        self.val = val
        self.next=next


class MutiTree():
    def __init__(self):
        self.Head=Node()

    def insert(self,id,pid,depth,val):
        cur=self.Head
        kdep=0
        if cur.id == pid:  # 创建根节点下面的子节点
            node = Node(id, val)
            cur.next.append(node)
        cur = cur.next
        flag=1
        while True:
            for k in range(cur):
                vcur=cur[k]
                if vcur is not object:
                    break
                if vcur.id==pid:
                    node = Node(id, val)
                    vcur.next.append(node)
                cur=vcur.next[k]
                if cur is not object:
                    flag=0
                break
            if flag==0:
                break



    def show(self):
        cur = self.Head
        print(cur.id)
        cur=cur.next
        for vcur in cur:
            if vcur is not object:
                break
            while True:
                print(vcur.id)
                vcur = vcur.next
                if vcur == [] :
                    break



data=[{'id':'1','val':'a','depth':1,'ord':1,'pid':'0'}, {'id':'11','val':'b','depth':2,'ord':1,'pid':'1'}, {'id':'12','val':'c','depth':2,'ord':2,'pid':'1'}]
Tree=MutiTree()
for i,v in enumerate(data):
    Tree.insert(data[i]['id'],data[i]['pid'],data[i]['val'])
Tree.show()




