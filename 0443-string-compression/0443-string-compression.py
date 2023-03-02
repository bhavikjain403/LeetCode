class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)
        i = 0
        while i < len(chars)-1:
            count = 1
            while i < len(chars)-1 and chars[i] == chars[i+1]:
                count += 1
                del chars[i]
            if count > 1:
                count = str(count)
                n = len(count)
                for j in range(n):
                    chars.insert(i+1+j, count[j])
                i += n+1
            else:
                i += 1