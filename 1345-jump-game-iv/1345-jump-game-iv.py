class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
        queue = deque([(0, 0)])
        visited, visited_groups = set(), set()
        while queue:
            steps, index = queue.popleft()
            if index == n - 1: return steps
            for j in [index - 1, index + 1]:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    queue.append((steps + 1, j))
            
            if arr[index] not in visited_groups:
                for neib in d[arr[index]]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append((steps + 1, neib))
                visited_groups.add(arr[index])