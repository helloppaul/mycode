'''
r 22-18-21-21-7-20 3-23-10-6;c;q0;p 1;b A6;c;b A5;b A1;c;q1;p 5;
r 25-9-1-1-12-20 7-3-8-14;p 10;p 10;b A3;c;b A1;q0;p 10;p 5;c;p 1;b A5;q0;
r 6-2-28-19-15-10 7-26-24-7;q0;b A2;c;q0;b A4;q1;b A5;q0;b A2;b A6;c;b A5;q1;q0;p 5;p 10;p 2;c;q0;p 2;p 5;q1;q1;p 5;p 5;c;p 5;p 1;b A3;p 5;c;b A3;p 5;
'''
def order(o,s):
    if o=='r':  #初始化操作
        a,b,c=s.split(' ')
        sys['stores'] = list(map(int, b.split('-')))
        # sys['storesNum'] = len(stores)
        sys['pockets'] = list(map(int, c.split('-')))
        print('S001:Initialization is successful')
    elif o=='p':  #投币操作
        a,b=s.split(' ')
        flag=1
        M={'1':0,'2':1,'5':2,'10':3}
        if b not in M:
            print('E002:Denomination error')
            flag=0
        pay = int(b)
        if sys['pockets'][0]*1 + sys['pockets'][1]*2 < pay and (pay not in [1, 2]):
            print('E003:Change is not enough, pay fail')
            flag = 0
        if sum(sys['stores']) == 0:
            print('E005:All the goods sold out')
            flag = 0
        if flag:
            sys['balance'] += pay
            sys['pockets'][M[str(pay)]] += 1
            print('S002:Pay success,balance=' + str(sys['balance']))
    elif o=='b':   #购买操作
        flag=1
        a,b=s.split(' ')
        idx=int(b[1])-1  #A1-> 下标0
        if idx>5:
            print('E006:Goods does not exist')
            flag=0
        if sys['stores'][idx]==0:
            print('E007:The goods sold out')
            flag=0
        if sys['balance']<sys['store_price'][idx]:
            print('E008:Lack of balance')
            flag=0
        if flag :
            sys['balance']-=sys['store_price'][idx]
            print('S003:Buy success,balance='+str(sys['balance']))
    elif o=='c':
        flag=1
        if sys['balance']==0:
            print('E009:Work failure')
            flag=0
        if flag:
            back={'1':0,'2':0,'5':0,'10':0}
            while sys['balance']>0:
                if sys['balance']-10>=0 and sys['pockets'][3]>0:
                    sys['balance']-=10
                    sys['pockets'][3] -= 1
                    back['10']+=1
                    continue
                if sys['balance']-5>=0 and sys['pockets'][2] >0:
                    sys['balance'] -= 5
                    sys['pockets'][2] -= 1
                    back['5']+=1
                    continue
                if sys['balance']-2>=0 and sys['pockets'][1]>0:
                    sys['balance'] -= 2
                    sys['pockets'][1] -= 1
                    back['2'] += 1
                    continue
                if sys['balance']-1>=0 and sys['pockets'][0]>0 :
                    sys['balance'] -= 1
                    sys['pockets'][0]-=1
                    back['1'] += 1
                    continue
                break
            for i in back:
                print(i,'yuan coin number='+str(back[i]))
            sys['balance']=0
    elif o=='q':   #查询操作
        try:
            a,b=s.split(' ')
        except:
            print('E010:Parameter error')
            return
        if b=='0':   #查询商品信息
            for i,storeNum in enumerate(sys['stores']):
                store='A'+str(i+1)
                price=sys[i]['store_price']
                print(store,price,storeNum)
        elif b=='1':   #存钱盒信息pockets
            M1={0:'1',1:'2',2:'5',3:'10'}
            for i,vnum in enumerate(sys['pockets']):   #每种钱币的张数
                print(M1[i]+'yuan coin number='+str(vnum))

while True:
    try:
        s=input().split(';')
        sys={'balance':0,'stores':[],'store_price':[2,3,4,5,8,6],'pockets':[]}  #系统参数 -> 商品数量,投币余额
        for v in s:
            if v:
                order(v[0],v)
    except:
        break