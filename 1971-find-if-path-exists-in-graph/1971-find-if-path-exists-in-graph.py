class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        q=deque()
        v=set()
        q.append(source)
        v.add(source)
        for i in edges:
            if i[0]==source:
                if i[1]==destination:
                    return True
                if i[1] not in v:
                    v.add(i[1])
                    q.append(i[1])
            if i[1]==source:
                if i[0]==destination:
                    return True
                if i[0] not in v:
                    v.add(i[0])
                    q.append(i[0])
        while len(q):
            n=q.popleft()
            for i in edges:
                if i[0]==n:
                    if i[1]==destination:
                        return True
                    if i[1] not in v:
                        v.add(i[1])
                        q.append(i[1])
                if i[1]==n:
                    if i[0]==destination:
                        return True
                    if i[0] not in v:
                        v.add(i[0])
                        q.append(i[0])
        return False