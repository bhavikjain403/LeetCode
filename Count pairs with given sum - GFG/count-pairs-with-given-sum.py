#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        d={}
        for i in arr:
            if d.get(i,0)==0:
                d[i]=1
            else:
                d[i]+=1
        ans=0
        for i in d:
            if i+i==k:
                ans+=(d[i]*(d[i]-1))//2
            else:
                if d.get(k-i,0):
                    ans+=d[i]*d[k-i]
                    d[i]=0
                    d[k-i]=0
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends