class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        Maxs=0
        for i in range(n):
            for j in range(n-1,i-1,-1):
                b=height[j]
                l=j-i
                s=l*min(height[i],height[j])
                if s>Maxs:
                    Maxs=s
        return Maxs