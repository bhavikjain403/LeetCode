class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for char in strs:
            arr = [0]*26
            for s in char:
                arr[ord(s) - ord("a")] += 1
            res[tuple(arr)].append(char)
        return res.values()