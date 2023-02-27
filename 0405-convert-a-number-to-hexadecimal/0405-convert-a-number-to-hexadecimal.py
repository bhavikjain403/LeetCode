class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = num + 2**32
        ans=""
        while num:
            r=num%16
            if r<10:
                ans+=str(r)
            else:
                ans+=chr(87+r)
            num//=16
        return ans[::-1]