class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        comb = nums[:k]+[n+1,0]
        ans = []
        while 1:
            ans.append(comb[:k])
            for i in range(len(comb)-1):
                if comb[i]+1==comb[i+1]:
                    comb[i]=i+1
                else:
                    break        
            if i<k:
                comb[i]+=1
            else:
                break
        return ans