class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d=dict()
        for i in range(26):
            d[chr(i+97)]=set()
        for i in ideas:
            d[i[0]].add(i[1:])
        ans=0
        for i in range(26):
            for j in range(i+1,26):
                common=len(d[chr(i+97)]&d[chr(j+97)])
                ans+=2*(len(d[chr(i+97)])-common)*(len(d[chr(j+97)])-common)
        return ans