class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[0]*(2*n)
        i=0
        j,k=0,n
        while i<2*n:
            ans[i]=nums[j]
            ans[i+1]=nums[k]
            i+=2
            j+=1
            k+=1
        return ans