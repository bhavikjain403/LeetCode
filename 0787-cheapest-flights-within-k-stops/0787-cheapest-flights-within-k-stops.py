class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d=defaultdict(set)
        for i in flights:
            d[i[0]].add((i[1],i[2]))
        q=deque()
        q.append((src,0,0))
        price={}
        for i in range(n):
            price[i]=float('inf')
        while q:
            node,cost,stops=q.popleft()
            if cost<=price[node] and stops<=k+1:
                price[node]=cost
                for data in d[node]:
                    q.append((data[0],data[1]+cost,stops+1))
        if price[dst]==float('inf'):
            return -1
        return price[dst]