class Solution:
    def fib(self, n: int) -> int:
        """滚动数组，可减小空间复杂度"""
        if n<2:
            return n
        p,q,r=0,0,1
        for i in range(2,n):
            p,q=q,r
            r=p+q
        return r
    def fib1(self, n: int) -> int:
        """dp做法"""
        dp=[0]*(n+1)
        if n>=1:
            dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-1]
        return dp[n]

print(Solution().fib(2))