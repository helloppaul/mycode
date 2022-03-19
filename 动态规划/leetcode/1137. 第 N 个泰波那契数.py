class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        elif n<3:
            return 1
        o,p,q,r=0,0,1,1
        for i in range(3,n+1):
            o,p,q=p,q,r
            r=o+p+q
        return r

r=Solution().tribonacci(4)
print(r)