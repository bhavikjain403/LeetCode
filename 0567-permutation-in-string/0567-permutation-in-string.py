class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        s1="".join(sorted(s1))
        l2=len(s2)
        i=0
        j=l1
        while j<=l2:
            while i<l2 and s2[i] not in s1:
                i+=1
                j+=1
            if j<=l2:
                t="".join(sorted(s2[i:j]))
                if s1==t:
                    return 1
                else:
                    i+=1
                    j+=1
        return 0