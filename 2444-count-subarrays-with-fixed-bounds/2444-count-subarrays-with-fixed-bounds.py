class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        mini = maxi = wrong = -1
        for i,a in enumerate(nums):
            if not minK <= a <= maxK: wrong = i
            if a == minK: mini = i
            if a == maxK: maxi = i
            res += max(0, min(mini, maxi) - wrong)
        return res