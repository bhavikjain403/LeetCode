class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = len(magazine)
        r = len(ransomNote)
        used = [0]*m
        for i in range(r):
            flag=1
            for j in range(m):
                if ransomNote[i]==magazine[j] and used[j]==0:
                    used[j]=1
                    flag=0
                    break
            if flag:
                return False
        return True