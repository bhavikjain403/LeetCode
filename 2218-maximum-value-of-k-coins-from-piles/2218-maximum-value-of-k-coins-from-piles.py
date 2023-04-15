class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        @lru_cache(None)
        def dp(n, k):
            if n == N:
                if k == 0: return 0
                if k > 0: return -float("inf")
            ans = dp(n + 1, k)
            sm = 0
            for i in range(min(k, len(piles[n]))):
                sm += piles[n][i]
                ans = max(ans, dp(n + 1, k - i - 1) + sm)
            return ans
        return dp(0, k)