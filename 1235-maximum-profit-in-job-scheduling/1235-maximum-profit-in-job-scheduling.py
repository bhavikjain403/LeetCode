class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0,0)]
        
        def find(time):
            size = len(dp)
            for i in range(size-1,-1,-1):
                pre_time = dp[i][0]
                if pre_time<=time:
                    return dp[i][1]
            
        for s, e, p in jobs:
            dp.append((e,max(find(e),find(s)+p)))
        return dp[-1][1]