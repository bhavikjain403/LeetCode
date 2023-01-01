class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        ls=len(s)
        lp=len(pattern)
        if ls==lp:
            for i in range(ls):
                for j in range(i+1,ls):
                    if s[i]==s[j]:
                        if pattern[i]!=pattern[j]:
                            return False
                    else:
                        if pattern[i]==pattern[j]:
                            return False
            return True
        return False