class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        if c1.keys()!=c2.keys():
            return False
        v1=list(c1.values())
        v2=list(c2.values())
        v1.sort()
        v2.sort()
        return v1==v2