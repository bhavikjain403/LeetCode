class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i,maxi=0,0
        l=len(nums)
        while i<=maxi:
            if maxi>=l-1:
                return True
            maxi=max(maxi,i+nums[i])
            i+=1
        return False