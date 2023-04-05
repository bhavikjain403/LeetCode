class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((a + i)//(i + 1) for i,a in enumerate(accumulate(nums)))