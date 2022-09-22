class Solution:
    def reverseWords(self, s: str) -> str:
        data=s.split(" ")
        ans=""
        l=len(data)
        for i in range(l):
            ans+=data[i][::-1]
            if i!=l-1:
                ans+=" "
        return ans