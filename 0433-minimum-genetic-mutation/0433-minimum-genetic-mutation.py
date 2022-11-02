class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = collections.deque([(start, 0)])
        seen = {start}
        while q:
            string, d = q.popleft()
            if string == end:
                return d
            for i in range(len(string)):
                for char in {"A","C","G","T"}:
                    if string[i] != char:
                        mutate = string[:i]+char+string[i+1:]
                        if mutate in bank and mutate not in seen:
                            seen.add(mutate)
                            q.append((mutate, d+1))
        return -1
        
        
            