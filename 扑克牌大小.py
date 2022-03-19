while True:
    try:
        a,b=input().split('-')
        arr1=a.split(' ')
        arr2=b.split(' ')
        la=len(arr1)
        lb=len(arr2)
        M={'JOKER':17,'joker':16,'A':14,'2':15,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
        if lb!=la:
            if 'joker' in arr1 or 'joker' in arr2:  #有一方是两张牌且是对王
                if 'joker' in arr1:
                    print(a)
                else:
                    print(b)
            elif la==4 or lb==4:   #有一方是四张牌(炸弹)，看炸弹实在哪一方，则那一方胜
                if la==4:
                    print(a)
                else:
                    print(b)
            else:
                print('ERROR')
        else:
            if la==5:
                if arr1[4]>arr2[4]:
                    print(a)
                else:
                    print(b)
            else:
                sc1 = 0
                sc2 = 0
                for v1 in arr1:
                    sc1+=M[v1]
                for v2 in arr2:
                    sc2 += M[v2]
                if sc1>sc2:
                    print(a)
                else:
                    print(b)
    except:
        break