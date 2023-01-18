class Solution:
    def maxsubarray(self,nums):
        cur,maxi=nums[0],nums[0]
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            maxi=max(cur,maxi)
        return maxi
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans1=self.maxsubarray(nums)
        ans2= sum(nums)+self.maxsubarray([-i for i in nums])
        if ans2==0:
            return ans1
        return max(ans1,ans2)