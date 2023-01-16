class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s,e=newInterval
        left,new,right=[],[],[]
        for i in intervals:
            if i[0]>e:
                right.append(i)
            elif i[1]<s:
                left.append(i)
            else:
                new.append(i)
        if new:
            s=min(new[0][0],s)
            e=max(new[-1][1],e)
        return left+[[s,e]]+right