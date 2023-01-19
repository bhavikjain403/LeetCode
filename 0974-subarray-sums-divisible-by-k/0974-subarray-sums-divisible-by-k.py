class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem={0:1}
        total=0
        ans=0
        for i in nums:
            total+=i
            if total%k in rem:
                ans+=rem[total%k]
                rem[total%k]+=1
            else:
                rem[total%k]=1
        return ans