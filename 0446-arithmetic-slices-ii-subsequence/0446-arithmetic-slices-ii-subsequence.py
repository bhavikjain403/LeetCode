class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        l = len(nums)
        for i in range(1,l): 
            for j in range(i):
                diff = nums[i]-nums[j]
                d[(i,diff)]+=d[(j,diff)]+1
                ans+=d[(j,diff)]
        return ans