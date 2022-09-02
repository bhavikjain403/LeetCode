class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates, target):
            if not candidates or target <= 0:
                return []
            res = []
            for i in range(len(candidates)-1, -1, -1):
                if i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                    continue
                elif candidates[i] == target:
                    res.append([target])
                tmp = helper(candidates[:i+1], target - candidates[i])
                res += [lst+[candidates[i]] for lst in tmp]
            return res
        
        candidates = sorted(candidates)
        return helper(candidates, target)