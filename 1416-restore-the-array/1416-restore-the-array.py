class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n = len(str(k)), len(s)
        dp = [1] * (n + 1)
		#find out number of ways for each ending.
        for i in range(n):
            res, cur = 0, ""
            for idx in range(i, max(-1, i - m), -1):
                cur = s[idx] + cur
                if cur[0] != "0" and int(cur) <= k:
                    res += dp[idx]
            if res == 0:
                return 0
            else:
                dp[i + 1] = res % (10 ** 9 + 7)
        return dp[-1]