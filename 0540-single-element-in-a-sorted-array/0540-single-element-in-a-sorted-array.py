class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,n-1
        while left<right:
            mid=(left+right)//2
            if (mid%2 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                left=mid+1
            else:
                right=mid
        return nums[left]