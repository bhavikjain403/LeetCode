class Solution:
    def reverseVowels(self, s: str) -> str:
        data=[]
        l=len(s)
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        for i in range(l-1,-1,-1):
            if s[i] in vowel:
                data.append(s[i])
        j=0
        s=list(s)
        for i in range(l):
            if s[i] in vowel:
                s[i]=data[j]
                j+=1
        return "".join(s)