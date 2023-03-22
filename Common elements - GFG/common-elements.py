#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i,j,k=0,0,0
        n=min(n1,n2,n3)
        ans=[]
        while i<n1 and j<n2 and k<n3:
            if A[i]<B[j]:
                i+=1
            elif B[j]<A[i]:
                j+=1
            else:
                while k<n3 and C[k]<A[i]:
                    k+=1
                if k<n3 and C[k]==A[i]:
                    if A[i] not in ans:
                        ans.append(A[i])
                i+=1
                j+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends