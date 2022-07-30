class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set(nums)
        return 2*sum(s)-sum(nums)