class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d=defaultdict(int)
        pL=len(p)
        sL=len(s)
        ans=[]
        if pL>sL:
            return []
        for ch in p:
            d[ch]+=1
        for i in range(pL-1):
            if s[i] in d:
                d[s[i]]-=1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in d:
                d[s[i]] += 1
            if i+pL < sL and s[i+pL] in d: 
                d[s[i+pL]] -= 1
            if all(v == 0 for v in d.values()): 
                ans.append(i+1)
        return ans