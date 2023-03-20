class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l,i=len(flowerbed),0
        while i<l-1:
            if flowerbed[i]==1:
                i+=2
            elif flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
                i+=2
            else:
                i+=1
        if flowerbed[l-1]==0 and flowerbed[l-2]==0:
            n-=1
        if n<=0:
            return True
        return False