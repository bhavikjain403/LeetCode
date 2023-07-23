class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)
        if l==1:
            if flowerbed[0]==0:
                if n<=1:
                    return True
                return False
            if n==0:
                return True
            return False
        i=0
        while i<l-1:
            if flowerbed[i]==0:
                if flowerbed[i+1]==0:
                    if i==0:
                        n-=1
                        flowerbed[i]=1
                    elif flowerbed[i-1]==0:
                        n-=1
                        flowerbed[i]=1
            i+=1
        if flowerbed[l-1]==0 and flowerbed[l-2]==0:
            n-=1
        if n<=0:
            return True
        return False