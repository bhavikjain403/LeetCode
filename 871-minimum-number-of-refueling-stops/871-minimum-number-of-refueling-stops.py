class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        data=[]
        stations.append((target,float('inf')))
        ans,prev=0,0
        for loc,cap in stations:
            startFuel-=loc-prev
            while data and startFuel<0:
                maxi=max(data)
                data.remove(maxi)
                startFuel+=maxi
                ans+=1
            if startFuel<0:
                return -1
            data.append(cap)
            prev=loc
        return ans