class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        i=0
        l=len(nums)
        while i<l:
            j=i
            while j<l-1 and nums[j+1]==nums[j]+1:
                j+=1
            if j==i:
                ans.append(f"{nums[i]}")
            else:
                ans.append(f"{nums[i]}->{nums[j]}")
            i=j+1
        return ans