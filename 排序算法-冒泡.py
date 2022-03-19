def BubbleSort(arr,ordflag):
    flag = 0
    larr = len(arr)
    if ordflag == 1:  #升序
        while flag == 0:
            flag=1
            for j in range(larr-1):
                if arr[j]>arr[j+1]:
                    tmp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=tmp
                    flag = 0
            if flag==1:
                break
    else:  #降序
        while flag == 0:
            flag=1
            for j in range(larr-1):
                if arr[j]<arr[j+1]:
                    tmp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=tmp
                    flag = 0
            if flag==1:
                break
    return arr

while True:
    try:
        orderArr=list(map(int,input().split(' ')))
        res=BubbleSort(orderArr,1)#顺序排列，从小到大
        print(res)
        res = BubbleSort(orderArr, 0)  # 顺序排列，从小到大
        print(res)
    except:
        break