class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        data = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        c1,c2=0,0
        for i in range(l):
            if i<l//2:
                if s[i] in data:
                    c1+=1
            else:
                if s[i] in data:
                    c2+=1
        return c1==c2