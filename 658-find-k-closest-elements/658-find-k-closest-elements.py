class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=len(arr)
        if l==k:
            return arr
        data=[]
        for i in arr:
            data.append([i,abs(i-x)])
        data=sorted(data, key=lambda x:x[1])
        ans=[]
        for i in range(k):
            ans.append(data[i][0])
        return sorted(ans)