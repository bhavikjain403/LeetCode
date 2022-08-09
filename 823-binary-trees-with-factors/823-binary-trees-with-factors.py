class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        l=len(arr)
        arr.sort()
        d={i: 1 for i in arr}
        for i in range(1,l):
            for j in range(i):
                q = arr[i]//arr[j]
                if q<2 or math.sqrt(arr[i]) > arr[i- 1]:
                    break
                if arr[i]%arr[j] == 0:
                    d[arr[i]] += d[arr[j]] * d.get(q, 0)
                    d[arr[i]]%=1000000007
        return sum(d.values())%1000000007