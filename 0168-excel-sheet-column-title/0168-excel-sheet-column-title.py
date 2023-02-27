class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""
        while columnNumber:
            ans+=chr(65+(columnNumber-1)%26)
            columnNumber=(columnNumber-1)//26
        return ans[::-1]