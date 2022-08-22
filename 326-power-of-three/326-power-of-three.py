class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return 0
        ans=1
        while ans<n:
            ans*=3
        if ans==n:
            return 1
        return 0