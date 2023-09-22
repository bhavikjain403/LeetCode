#User function Template for python3

class Solution:
    def check(self,mid,arr,n,k):
        s,c=0,0
        for i in arr:
            if i>mid:
                return False
            s+=i
            if s>mid:
                c+=1
                s=i
        c+=1
        return c<=k
        
    def splitArray(self, arr, N, K):
        start,end=max(arr),sum(arr)
        ans=0
        while start<=end:
            mid=(start+end)//2
            if self.check(mid,arr,N,K):
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