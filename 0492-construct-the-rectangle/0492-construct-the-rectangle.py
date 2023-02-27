class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l,w=area,1
        diff=l-w
        for x in range(1,area//2+1):
            if area%x==0:
                y=area//x
                if diff>abs(y-x):
                    diff=abs(y-x)
                    l,w=max(x,y),min(x,y)
        return [l,w]