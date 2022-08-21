class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        if n==0:
            return 1
        keys=[[0]]
        vis=[0]*n
        while keys:
            p=keys.pop(0)
            for i in p:
                if vis[i]==0:
                    vis[i]=1
                    keys.append(rooms[i])
        for i in vis:
            if i==0:
                return 0
        return 1