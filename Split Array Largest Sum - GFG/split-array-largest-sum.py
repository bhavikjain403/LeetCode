#User function Template for python3

class Solution:
    def valid(self,mid,arr,k):
        ans=0
        count=0
        for i in arr:
            if i>mid:
                return False
            ans+=i
            if ans>mid:
                count+=1
                ans=i
        count+=1
        if count<=k:
            return True
        return False
    
    def splitArray(self, arr, N, K):
        start,end=max(arr),sum(arr)
        answer=0
        while start<=end:
            mid=(start+end)//2
            if self.valid(mid,arr,K):
                end=mid-1
                answer=mid
            else:
                start=mid+1
        return answer


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