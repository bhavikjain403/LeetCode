class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for i in queries:
            total=0
            temp=0
            for j in nums:
                if total+j<=i:
                    total+=j
                    temp+=1
                else:
                    break
            ans.append(temp)
        return ans