class Solution:
    def deleteAndEarn(self, nums) :  #滚动数组
        max_=(max(nums)+1)
        all=[0]*max_
        for v in nums:
            all[v]+=1
        if max_==1:

        p,q,r=0,all[1]*1,0
        for i in range(2,max_):
            r=max(p+all[i]*i,q)
            p,q=q,r
        return r
    def deleteAndEarn1(self, nums) :  #标准解
        max_=(max(nums)+1)
        all=[0]*max_
        for v in nums:
            all[v]+=1
        dp=[0]*max_
        dp[0]=0
        dp[1]=all[1]*1
        for i in range(2,max_):
            dp[i]=max(dp[i-2]+all[i]*i,dp[i-1])
        return dp[max_-1]

# arr=[3,4,2]
arr=[2,2,3,3,3,4]
r=Solution().deleteAndEarn(arr)
print(r)