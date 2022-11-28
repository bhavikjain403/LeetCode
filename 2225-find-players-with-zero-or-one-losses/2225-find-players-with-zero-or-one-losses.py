class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d=dict()
        for i in matches:
            d[i[0]]=0
            d[i[1]]=0
        for i in matches:
            d[i[1]]+=1
        l1,l2=[],[]
        for i in d:
            if d[i]==0:
                l1.append(i)
            if d[i]==1:
                l2.append(i)
        l1.sort()
        l2.sort()
        return [l1,l2]