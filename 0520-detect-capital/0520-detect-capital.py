class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l=len(word)
        if l==1:
            return True
        if l==2 and word[0]==word[0].upper():
            return True
        if word[0]==word[0].lower():
            for i in range(1,l):
                if word[i]==word[i].upper():
                    return False
            return True
        if word[1]==word[1].lower():
            for i in range(2,l):
                if word[i]==word[i].upper():
                    return False
            return True
        for i in range(2,l):
            if word[i]==word[i].lower():
                return False
        return True