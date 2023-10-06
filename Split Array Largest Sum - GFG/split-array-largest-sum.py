#User function Template for python3

class Solution:
    def valid(self,mid,arr,k):
        count=0
        ans=0
        for i in arr:
            if i>mid:
                return False
            ans+=i
            if ans>mid:
                ans=i
                count+=1
        count+=1
        return count<=k
    
    def splitArray(self, arr, N, K):
        start,end=max(arr),sum(arr)
        ans=0
        while start<=end:
            mid=(start+end)//2
            if self.valid(mid,arr,K):
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends