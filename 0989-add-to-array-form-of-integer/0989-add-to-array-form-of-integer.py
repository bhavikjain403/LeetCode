class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=int("".join(str(i) for i in num))+k
        data=[]
        while ans:
            data.append(ans%10)
            ans//=10
        return data[::-1]