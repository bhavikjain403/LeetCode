class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @cache 
        def dp(i, k, prev, cnt):
            """Return length of rle of s[i:] with k chars to be deleted."""
            if k < 0: return inf 
            if i == len(s): return 0 
            ans = dp(i+1, k-1, prev, cnt) # delete current character 
            if prev == s[i]: 
                delta = (0 if cnt not in [9, 99] else 1) #if 9-10 or 99-100 we need to increase the len by 1
                delta += 1 if cnt==1 else 0 #for first char
                ans = min(ans, dp(i+1, k, s[i], cnt+1) +  delta)
            else: 
                ans = min(ans, dp(i+1, k, s[i], 1) + 1)
            return ans 
        
        return dp(0, k, "", 0)