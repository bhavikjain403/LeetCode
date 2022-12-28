class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[-i for i in piles]
        heapify(heap)
        while k and heap:
            x=-1*heappop(heap)
            heappush(heap,-x//2)
            k-=1
        return -1*sum(heap)