class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas): 
            return -1
        n,start,g=len(gas),0,0
        for i in range(n):
            g+=gas[i]-cost[i]
            if g<0:
                start,g=i+1,0
        return start