class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(n):
            q = deque([n])
            l=len(edges)
            d = [l+10]*l
            d[n] = 0
            while q:
                i = q.popleft()
                nxt = edges[i]
                if nxt!=-1 and d[nxt]>l:
                    q.append(nxt)
                    d[nxt] = d[i]+1 
            return d

        d1, d2 = bfs(node1), bfs(node2)
        dist, idx = len(edges)+10, -1
        for i in range(len(edges)):
            if dist > max(d1[i], d2[i]):
                dist, idx = max(d1[i], d2[i]), i
        return idx