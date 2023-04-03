class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low,high=0,len(people)
        ans=0
        while low<high:
            ans+=1
            high-=1
            if people[low]+people[high]<=limit:
                low+=1
        return ans