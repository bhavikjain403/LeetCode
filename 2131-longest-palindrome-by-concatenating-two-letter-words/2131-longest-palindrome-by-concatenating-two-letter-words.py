class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c=defaultdict(int)
        ans=0
        for i in words:
            if c[i[1]+i[0]]>0: 
                c[i[1]+i[0]]-=1
                ans+=4
            else:
                c[i]+=1
        for i in c.keys(): 
            if i[0]==i[1] and c[i]>0:
                ans+=2
                break
        return ans