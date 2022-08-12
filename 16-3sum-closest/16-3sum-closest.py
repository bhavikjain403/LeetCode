class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = math.inf
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                sum_val = nums[i]+nums[j]+nums[k]
                if(abs(sum_val-target)<abs(ans-target)):
                    ans = sum_val
                if(sum_val<target):
                    j+=1
                elif(sum_val>target):
                    k-=1
                else:
                    return target
        return ans