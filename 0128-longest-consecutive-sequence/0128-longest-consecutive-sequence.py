class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set(nums)
        ans=1
        for i in nums:
            if i-1 not in s:
                temp=1
                cpy=i
                while cpy+1 in s:
                    cpy+=1
                    temp+=1
                ans=max(ans,temp)
        return ans