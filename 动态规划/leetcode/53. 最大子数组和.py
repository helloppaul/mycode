class Solution:
    def maxSubArray_devide(self, nums):  #线段树-分治法
        res=[]
        def get(nums, l, r):
            if l==r:
                return [nums[l],nums[l],nums[l],nums[l]]  #isum,lsum,rsum,msum
            m=(l+r)//2
            get(nums,l,m)
            get(nums,m+1,r)
        return get(nums,nums[0],nums[len(nums)-1])



    def maxSubArray(self, nums):
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        Max=nums[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            if dp[i]>Max:
                Max=dp[i]
        return Max


arr=[-2,1,-3,4,-1,2,1,-5,4]
r=Solution().maxSubArray(arr)