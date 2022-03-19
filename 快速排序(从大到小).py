def partition(arr,low,high):
    i=low #最小元素索引
    pivot=arr[high]

    for j in range(low,high):
        if arr[j]>=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
    arr[i],arr[high]=arr[high],arr[i]
    return i  #返回 排序后 基准的下标

def quickSort(arr,low,high):
    if low < high:
        pi=partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)



arr = [10, 7, 8, 9, 1, 5]

n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i]),