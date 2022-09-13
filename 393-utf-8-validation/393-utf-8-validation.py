class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(cur):
            tmp, digits = 0, 128
            while digits and digits & cur:
                tmp, digits = tmp + 1, digits >> 1
            return tmp
        
        data = [x & 255 for x in data]
        i, n = 0, len(data)
        while i < n:
            j = check(data[i])
            if not j: i += 1
            elif 1 < j < 5 and i + j <= n and all(check(data[x]) == 1 \
            for x in range(i+1, i+j)): i += j
            else: return False
        return True