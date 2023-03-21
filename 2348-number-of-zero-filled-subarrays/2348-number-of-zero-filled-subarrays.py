class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans,i,n=0,0,len(nums)
        while i<n:
            temp=0
            while i<n and nums[i]==0:
                temp+=1
                i+=1
            ans+=(temp*(temp+1))//2
            i+=1
        return ans