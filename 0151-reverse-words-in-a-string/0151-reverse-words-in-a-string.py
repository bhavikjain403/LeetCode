class Solution:
    def reverseWords(self, s: str) -> str:
        l=len(s)
        i=0
        words,lw=[],0
        while i<l:
            if s[i]!=" ":
                j=i
                while j<l and s[j]!=" ":
                    j+=1
                words.append(s[i:j])
                lw+=1
                i=j+1
            else:
                i+=1
        ans=""
        for i in range(lw-1,-1,-1):
            ans+=words[i]
            if i>0:
                ans+=" "
        return ans