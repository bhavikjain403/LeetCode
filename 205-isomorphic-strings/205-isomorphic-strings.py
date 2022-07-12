class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        rep = dict()
        used = dict()
        n = len(s)
        for i in range(n):
            if s[i] in rep.keys():
                if rep[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in used.keys() and used[t[i]]:
                    return False
                rep[s[i]]=t[i]
                used[t[i]]=True
        return True