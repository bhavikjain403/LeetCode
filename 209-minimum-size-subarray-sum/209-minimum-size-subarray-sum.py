class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = total = 0
        res = len(nums) + 1
        for i in range(len(nums)):
            total = total + nums[i]
            while total >= s:
                res = min(res,i-left+1)
                total = total - nums[left]
                left = left+1
        return res if res <= len(nums) else 0