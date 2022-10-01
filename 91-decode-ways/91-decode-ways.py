class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1] if i-1 >= 0 else 1
            if i-1 >= 0 and int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) >= 10:
                dp[i] += dp[i-2] if i-2 >= 0 else 1
        return dp[len(s)-1]