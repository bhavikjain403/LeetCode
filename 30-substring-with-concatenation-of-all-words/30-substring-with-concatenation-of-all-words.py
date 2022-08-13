class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m = len(words)
        k = len(words[0])
        res = []
        for i in range(k):
            left = i
            d = Counter(words)
            for j in range(left, len(s) + 1 - k, k):
                word = s[j: j + k]
                d[word] -= 1
                
                while d[word] < 0:
                    d[s[left: left + k]] += 1
                    left += k
                if left + k * m == j + k:
                    res. append(left)
        return res