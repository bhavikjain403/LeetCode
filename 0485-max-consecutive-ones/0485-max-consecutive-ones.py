class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans,i,n=0,0,len(nums)
        while i<n:
            temp=0
            while i<n and nums[i]==1:
                temp+=1
                i+=1
            ans=max(ans,temp)
            i+=1
        return ans