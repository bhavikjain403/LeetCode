class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return 0
        data=[nums[0]]
        for i in range(1,l):
            data.append(data[i-1]+nums[i])
        ans,idx=float('inf'),-1
        for i in range(l):
            left=data[i]//(i+1)
            if l-i-1>0:
                right=(data[l-1]-data[i])//(l-i-1)
            else:
                right=0
            temp=abs(left-right)
            if temp<ans:
                ans=temp
                idx=i
        return idx