class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        c = 0
        for i in nums:
            if c<0:
                c=0
            c+=i
            m = max(m,c)
        return m