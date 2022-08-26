class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        i,arr=0,[]
        v=2**i
        cpy=n
        d=0
        while cpy:
            d+=1
            cpy=cpy//10
        while v<=10**(d+1):
            arr.append(sorted(str(v)))
            i+=1
            v=2**i
        return sorted(str(n)) in arr