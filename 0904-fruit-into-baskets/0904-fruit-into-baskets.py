class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        if n<=2:
            return n
        ans=0
        i=0
        while i<n-1:
            temp=1
            j=i+1
            a,b=fruits[i],fruits[j]
            if a==b:
                flag=0
            else:
                flag=1
                idx=j
            while j<n:
                if flag==1 and fruits[j]!=a and fruits[j]!=b:
                    i=idx
                    break
                if flag==0 and fruits[j]!=a:
                    b=fruits[j]
                    flag=1
                    idx=j
                temp+=1
                j+=1
            ans=max(ans,temp)
            if j==n:
                break
        return ans