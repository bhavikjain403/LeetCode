class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            s=nums.index(target)
            l=len(nums)
            if nums[l-1]==target or s==l-1:
                return [s,l-1]
            e=s
            for i in range(s+1,l):
                if nums[i]==target:
                    e+=1
                else:
                    break
            return [s,e]
        return [-1,-1]