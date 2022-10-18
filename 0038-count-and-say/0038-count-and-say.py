class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        if n == 1:
            return res
        for i in range(2,n+1):
            ans = []
            charPointer = res[0]
            countPointer = 0
            for char in res:
                if char == charPointer:
                    countPointer += 1
                else:
                    ans.append(str(countPointer))
                    ans.append(charPointer)
                    charPointer = char
                    countPointer = 1
            ans.append(str(countPointer))
            ans.append(charPointer)
            res = "".join(ans)
        return res