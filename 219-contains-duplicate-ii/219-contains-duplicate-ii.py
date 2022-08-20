class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=len(nums)
        if l==len(set(nums)):
            return 0
        if k>=l-1:
            return 1
        for i in range(l-1):
            temp=nums[i+1:]
            if nums[i] in temp:
                if 1+temp.index(nums[i])<=k:
                    return 1
        return 0