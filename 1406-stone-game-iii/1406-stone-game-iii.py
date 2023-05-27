class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[(i + 1) % 3]
            take_two = float('-inf')
            if i + 1 < n:
                take_two = stoneValue[i] + stoneValue[i + 1] - dp[(i + 2) % 3]
            take_three = float('-inf')
            if i + 2 < n:
                take_three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[(i + 3) % 3]
            dp[i % 3] = max(take_one, take_two, take_three)
        score_diff = dp[0]
        if score_diff > 0:
            return "Alice"
        elif score_diff < 0:
            return "Bob"
        else:
            return "Tie"