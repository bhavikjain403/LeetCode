class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        l=len(stones)
        if l==1:
            return stones[0]
        while l>1:
            if stones[0]==stones[1]:
                stones=stones[2:]
                l-=2
            elif stones[0]>stones[1]:
                stones[0]-=stones[1]
                stones.pop(1)
                stones.sort(reverse=True)
                l-=1
            elif stones[0]<stones[1]:
                stones[1]-=stones[0]
                stones.pop(0)
                stones.sort(reverse=True)
                l-=1
            if l==1:
                return stones[0]
        return 0