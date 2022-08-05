class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        if digits[l-1]!=9:
            digits[l-1]+=1
            return digits
        if digits.count(9)==l:
            for i in range(l):
                digits[i]=0
            digits[0]=1
            digits.append(0)
            return digits
        while digits[l-1]==9:
            digits[l-1]=0
            l-=1
        digits[l-1]+=1
        return digits