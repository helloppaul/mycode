'''
3
0
fang 90
yang 50
ning 70
~
fang 90
ning 70
yang 50
'''
def maopao(arr,ord,k):
    if ord == 0:  # 倒序
        while True:
            flag = 0
            for i in range(len(arr) - 1):
                if int(arr[i][k]) < int(arr[i + 1][k]):
                    tmp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = tmp
                    flag = 1
            if flag == 0:
                break
    else:
        while True:
            flag = 0
            for i in range(len(arr) - 1):
                if int(arr[i][k]) > int(arr[i + 1][k]):
                    tmp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = tmp
                    flag = 1
            if flag == 0:
                break
    return arr


while True:
    try:
        n=int(input())
        ord=int(input())
        slist=[]
        for i in range(n):
            slist.append(input().split(' '))
        maopao(slist,ord,1)
        for i in range(n):
            print(slist[i][0],slist[i][1])
    except:
        break