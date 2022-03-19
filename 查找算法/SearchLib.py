class Search():
    def binarySearch(self, nums=[], find=None):
        "常规二分查找"
        left = 0
        right = len(nums) - 1  # 因为right是数组长度-1，所以索索区间为[left,right]。故 while left<=right，若为left<right,搜索区间为[left,right)少了right没搜索
        while left <= right:  # 注意！此处需要<=。若为<，表示当left>=right时停止,即left=right,[right,right]或者[left,left]停止，漏掉了right或者left没有搜索。
            mid = int((left + right) / 2)  # 类似直角坐标系中点(x1+x2)/2
            if nums[mid] == find:
                return mid  # 返回find值在nums序列中的索引
            elif find < nums[mid]:  # find小,find值在nums[mid]的左侧
                right = mid - 1
            elif nums[mid] < find:  # find大,find值在nums[mid]的右侧
                left = mid + 1
        return -1

    def binarySearch_leftbound(self, nums=[], find=None):
        "左侧边界值的二分查找。若找到，则返回在查找列表最左侧且等于find值的下标；反之，返回-1"
        Lnums = len(nums)
        left = 0
        right = Lnums  # [left,right)
        while left < right:  # 停止条件left=right,[left,left)时，搜索空间为空，正好停止
            mid = int((left + right) / 2)
            if nums[mid] == find:
                right = mid
            elif find < nums[mid]:
                right = mid
            elif nums[mid] < find:
                left = mid + 1
        if left == Lnums:  # 待查找值不存在且大于查找列表最大值
            return -1
        return left if nums[left] == find else -1  # 待查找值不存在且小于查找列表最小值

    def binarySearch_rightbound(self, nums=[], find=None):
        "左侧边界值的二分查找。若找到，则返回的是在查找列表最右侧且等于find值的下标；反之，返回-1"
        Lnums = len(nums)
        left = 0
        right = Lnums  # [left,right)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == find:
                left = mid + 1
            elif find < nums[mid]:
                right = mid
            elif nums[mid] < find:
                left = mid + 1
        if left == 0:  # 如果有边界值的话,left至少是1
            return -1
        return left - 1 if nums[left - 1] == find else -1

    def leftbound(self, nums=[], find=None):
        "左侧边界值的二分查找，返回小于find值的最大元素下标 或 返回等于find值的最小边界下标"
        Lnums = len(nums)
        left = 0
        right = Lnums  # [left,right)
        while left < right:  # 停止条件left=right,[left,left)时，搜索空间为空，正好停止
            mid = int((left + right) / 2)
            if nums[mid] == find:
                right = mid
            elif find < nums[mid]:
                right = mid
            elif nums[mid] < find:
                left = mid + 1
        if left==Lnums or nums[left]!=find:
            return left-1
        return left
    def rightbound(self, nums=[], find=None):
        "右侧边界值的二分查找，返回大于find值时最小元素下标 或 返回等于find值时最大边界下标"
        Lnums = len(nums)
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
        if left==0 or nums[left-1]!=find:  #没有搜索到find值时的返回
            return left
        return left-1   #搜索到find值时的返回


a = Search()
print(a.rightbound([2, 3, 4, 7, 8, 10], 1))
# print(a.leftbound([1, 3, 3, 5], 3))
# # print(a.binarySearch([1,3,4,7,8,10],3))
# # print(a.binarySearch_leftbound([2,2,5,7],2))
# print(a.my_rightbound([1,1,2,2,3],3))
