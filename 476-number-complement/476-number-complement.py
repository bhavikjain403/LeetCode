class Solution:
    def findComplement(self, num: int) -> int:
        num=list(bin(num)[2:])
        l=len(num)
        for i in range(l):
            if num[i]=="0":
                num[i]="1"
            else:
                num[i]="0"
        return int("".join(num),2)