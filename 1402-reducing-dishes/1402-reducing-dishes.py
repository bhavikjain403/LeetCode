class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1]+total>0:
            total += satisfaction.pop()
            ans += total
        return ans