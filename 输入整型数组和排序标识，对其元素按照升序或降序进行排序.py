def maopao(arr,ord):
    if ord==0:  #升序
        while True:
            flag=1
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    flag=0
            if flag:
                break
    else:
        while True:
            flag=1
            for i in range(len(arr)-1):
                if arr[i]<arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    flag=0
            if flag:
                break
    return arr
while True:
    try:
        n=int(input())
        arr=list(map(int,input().split(' ')[:n]))
        ord=int(input())
        print(' '.join(map(str,maopao(arr,ord))))
    except:
        break