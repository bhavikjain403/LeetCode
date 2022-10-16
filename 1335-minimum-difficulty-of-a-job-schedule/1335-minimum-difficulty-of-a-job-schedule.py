class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        job_count = len(jobDifficulty)
        if job_count < d:
            return -1

        @lru_cache(None)
        def min_score(last_score=0, cur_idx=0, div_left=d-1):
            if div_left == 0: return max([last_score] + jobDifficulty[cur_idx:])
            cur_score = max(last_score, jobDifficulty[cur_idx])
            if job_count - cur_idx == div_left + 1:
                return cur_score + sum(jobDifficulty[cur_idx+1:])
            join_score = min_score(cur_score, cur_idx+1, div_left)
            div_score = cur_score + min_score(0, cur_idx+1, div_left-1)
            return min(join_score, div_score)

        return min_score()