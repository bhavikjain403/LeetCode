#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        ans=max(arr)-min(arr)
        arr.sort()
        small,large=arr[0]+k,arr[n-1]-k
        for i in range(n):
            if arr[i]<k:
                continue
            minH=min(small,arr[i]-k)
            maxH=max(arr[i-1]+k,large)
            ans=min(ans,maxH-minH)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends