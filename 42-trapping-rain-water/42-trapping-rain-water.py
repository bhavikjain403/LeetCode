class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        left=[]
        right=[]
        maxi=0
        for i in range(l):
            maxi=max(maxi,height[i])
            left.append(maxi)
        maxi=0
        for i in range(l-1,-1,-1):
            maxi=max(maxi,height[i])
            right.append(maxi)
        right=right[::-1]
        ans=0
        for i in range(l):
            diff=min(left[i],right[i])
            ans+=diff-height[i]
        return ans