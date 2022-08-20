class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return 0
        if log(n,4)==int(log(n,4)):
            return 1
        return 0