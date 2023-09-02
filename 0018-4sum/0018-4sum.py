class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=set()
        if not nums:
            return []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                cur=nums[i]+nums[j]
                left,right=j+1,len(nums)-1
                while left<right:
                    total=cur+nums[left]+nums[right]
                    if total==target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    else:
                        if total<target:
                            left+=1
                        else:
                            right-=1
        return ans