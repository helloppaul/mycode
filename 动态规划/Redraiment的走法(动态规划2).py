'''
6
2 5 1 5 4 5
:3
~
30
186 13 322 264 328 110 120 73 20 35 240 97 150 221 284 324 46 219 239 284 128 251 298 319 304 36 144 236 163 122
:10
解题思路：动态规划 + 贪心算法 + 二分法查找边界值
dp[i]:当步长为i时，末尾元素最小时的最大上升子序列
'''
def rightbound(nums=[], find=None,L=None):
    "右侧边界值的二分查找，返回大于find值时最小元素下标 或 返回等于find值时最大边界下标"
    Lnums = L if L else len(nums)
    left = 0
    right = Lnums  # [left,right)
    while left < right:  # 停止条件left=right,[left,left)时，搜索空间为空，正好停止
        mid = int((left + right) / 2)
        if nums[mid] == find:
            left = mid + 1
        elif find < nums[mid]:
            right = mid
        elif nums[mid] < find:
            left = mid + 1
    if left == 0 or nums[left - 1] != find:  # 没有搜索到find值时的返回
        return left
    return left - 1  # 搜索到find值时的返回
while True:
    try:
        n = int(input())
        arr = list(map(int, input().split(' ')[:n]))
        dp=[arr[0]]
        k=0
        for i in range(1,n):
            if dp[k]<arr[i]:
                dp.append(arr[i])
                k += 1
            else:
                idx=rightbound(dp,arr[i],k+1)
                dp[idx]=arr[i]
        print(k+1)
    except:
        break