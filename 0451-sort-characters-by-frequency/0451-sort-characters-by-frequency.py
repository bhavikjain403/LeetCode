class Solution:
    def frequencySort(self, s: str) -> str:
        data=Counter(s).most_common(len(set(s)))
        ans=""
        for i,j in data:
            ans+=i*j
        return ans