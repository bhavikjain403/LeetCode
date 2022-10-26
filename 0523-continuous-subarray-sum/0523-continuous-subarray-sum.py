class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen,cur={0: -1},0
        for i,a in enumerate(nums):
            cur=(cur+a)%k
            if i-seen.setdefault(cur,i)>1:
                return 1
        return 0