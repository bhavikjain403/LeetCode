class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[-1]
        arr.append(-1)
        ans=0
        l=len(arr)
        for i in range(l):
            while arr[i]<arr[stack[-1]]:
                idx=stack.pop()
                ans+=arr[idx]*(i-idx)*(idx-stack[-1])
            stack.append(i)
        return ans%(10**9+7)