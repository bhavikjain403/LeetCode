class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        i=0
        j=len(height)-1
        while i<j:
            ans=max((j-i)*min(height[i],height[j]),ans)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ans