class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq, [i//(i&-i),i])
        ans=float('inf')
        maxi=max(i for i,j in pq)
        lp,ln=len(pq),len(nums)
        while lp==ln:
            i,j=heapq.heappop(pq)
            lp-=1
            ans=min(ans,maxi-i)
            if i%2 or i<j:
                maxi=max(maxi,i*2)
                heapq.heappush(pq, [i*2,j])
                lp+=1
        return ans