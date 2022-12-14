class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        nonadj=nums[0]
        adj=max(nums[0],nums[1])
        for i in range(2,l):
            c=max(nums[i]+nonadj,adj)
            nonadj=adj
            adj=c
        return adj