class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        data = list(zip(scores, ages))
        data.sort()
        dp = [i[0] for i in data]
        for i in range(1, len(data)):
            for j in range(i):
                if data[j][1] <= data[i][1]:
                    dp[i] = max(dp[i], dp[j] + data[i][0])
        return max(dp)