class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        if a==a[::-1]:
            return 1
        return 0