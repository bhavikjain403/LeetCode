class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        @lru_cache(None)
        def dfs(r1,c1,K):
            total, ans = 0, 0
            for i in range(r1,m):
                for j in range(c1,n):
                    if pizza[i][j] == "A":
                        total += 1
            if K == 0:
                return int(total != 0)
            sum_hor_cuts = 0
            for i in range(r1,m-1):
                for j in range(c1,n):
                    if pizza[i][j] == "A":
                        sum_hor_cuts += 1
                if sum_hor_cuts > 0:
                    ans += dfs(i+1,c1,K-1)
            sum_ver_cuts = 0
            for j in range(c1,n-1):
                for i in range(r1,m):
                    if pizza[i][j] == "A":
                        sum_ver_cuts += 1
                if sum_ver_cuts > 0:
                    ans += dfs(r1,j+1,K-1)
            return ans
        return dfs(0,0,k-1)%(10**9+7)