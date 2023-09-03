class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # pre=[]
        # m,n=len(mat),len(mat[0])
        # for i in range(m+1):
        #     pre.append([0]*(n+1))
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         pre[i][j]=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+mat[i-1][j-1]
        # lo,hi=0,min(m,n)
        # while lo<=hi:
        #     mid=(lo+hi)//2
        #     flag=0
        #     for i in range(mid,m+1):
        #         for j in range(mid,n+1):
        #             if(pre[i][j]+pre[i-mid][j-mid]-pre[i-mid][j]-pre[i][j-mid]<=threshold):
        #                 flag=1
        #                 break
        #         if flag:
        #             break
        #     if flag:
        #         lo=mid+1
        #     else:
        #         hi=mid-1
        # return hi
        
        pre=[]
        m,n=len(mat),len(mat[0])
        for i in range(m+1):
            pre.append([0]*(n+1))
        for i in range(1,m+1):
            for j in range(1,n+1):
                pre[i][j]=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+mat[i-1][j-1]
        lo,hi=0,min(m,n)
        while lo<=hi:
            mid=(lo+hi)//2
            flag=0
            for i in range(mid,m+1):
                for j in range(mid,n+1):
                    if pre[i][j]+pre[i-mid][j-mid]-pre[i-mid][j]-pre[i][j-mid]<=threshold:
                        flag=1
                        break
                if flag:
                    break
            if flag:
                lo=mid+1
            else:
                hi=mid-1
        return hi
        