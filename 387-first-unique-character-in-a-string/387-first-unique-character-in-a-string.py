class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        for i in range(l):
            flag=1
            for j in range(i+1,l):
                if s[i]==s[j]:
                    flag=0
                    break
            for j in range(0,i):
                if s[i]==s[j]:
                    flag=0
                    break
            if flag:
                return i
        return -1