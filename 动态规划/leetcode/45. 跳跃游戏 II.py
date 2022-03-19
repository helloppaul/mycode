class Solution:
    def jump_1(self,nums):
        """贪心算法，正向查找，O(n)"""
        n=len(nums)
        maxPos,step,end=0,0,0 #初始化
        for i in range(n-1):
            maxPos = max(maxPos, i + nums[i])
            if i==end:
                end=maxPos
                step+=1
        return step



    def jump_0(self,nums):
        """贪心算法，考虑从最后一个位置开始跳到最远的距离"""
        n=len(nums)
        jump=0
        i=0
        y=n-1
        while y>0:
            if i+nums[i]>=y:
                jump+=1
                y=i
                i=-1
            i+=1
        return jump

    def jump_my(self, nums) :
        """超时"""
        n=len(nums)
        #dp[i]表示跳到第i个位置的最小跳跃次数
        dp=[1]*n
        dp[0]=0
        for i in range(n):
            k=0
            for j in range(i):
                if j+nums[j]>=i:
                    if k==0:
                        dp[i]=dp[j]+1
                        k+=1
                    else:
                        dp[i]=min(dp[i],dp[j]+1)
        return dp[n-1]

# r=Solution().jump_my([2,3,1,1,4])
# r=Solution().jump_0([2,3,1,1,4])
r=Solution().jump_1([2,3,1,1,4])
print(r)
