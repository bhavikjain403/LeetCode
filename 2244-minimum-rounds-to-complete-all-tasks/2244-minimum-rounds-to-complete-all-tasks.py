class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c=Counter(tasks)
        ans=0
        for i in c:
            if c[i]==1:
                return -1
            ans+=c[i]//3
            if c[i]%3:
                ans+=1
        return ans