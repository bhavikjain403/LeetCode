class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def recurse(c,start):
            if len(c)>1:
                ans.add(tuple(c))
            for i in range(start,len(nums)):
                if not c or c[-1]<=nums[i]:
                    recurse(c+[nums[i]],i+1)
                else:
                    recurse(c,i+1)
        recurse([],0)
        return list(ans)