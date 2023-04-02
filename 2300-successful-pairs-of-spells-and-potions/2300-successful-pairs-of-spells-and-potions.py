class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[0]*len(spells)
        for i in range(len(spells)):
            ans[i]=len(potions)-bisect_left(potions,(success+spells[i]-1)//spells[i])
        return ans