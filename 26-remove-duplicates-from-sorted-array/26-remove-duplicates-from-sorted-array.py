class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        i=1
        l=len(nums)
        while i<l:
            if nums[i]==nums[i-1]:
                nums.pop(i)
                l-=1
            else:
                i+=1
                k+=1
        return k