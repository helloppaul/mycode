def maopao(arr):
    while 1:
        flag=0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=1
        if flag==0:
            break
    return arr
while True:
    try:
        n1=int(input())
        nums1=list(map(int,input().split(' ')))
        n2=int(input())
        nums2=list(map(int,input().split(' ')))
        nums=list(set(nums1+nums2))
        res=maopao(nums)
        print(''.join(map(str,res)))
    except:
        break