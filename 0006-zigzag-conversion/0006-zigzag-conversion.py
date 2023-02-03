class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        if n<=numRows:
            return s
        if numRows==1:
            return s
        if numRows==2:
            i=0
            ans1,ans2="",""
            while i<n:
                ans1+=s[i]
                if i+1<n:
                    ans2+=s[i+1]
                i+=2
            return ans1+ans2
        col=0
        i=0
        while i<n:
            col+=1
            i+=numRows
            c=numRows-2
            while c:
                if i<n:
                    i+=1
                    col+=1
                else:
                    break
                c-=1
        table=[]
        for i in range(numRows):
            temp=[]
            for j in range(col):
                temp.append("")
            table.append(temp)
        zigzag=numRows-2
        c=0
        i,j=0,0
        down=1
        while c<n:
            if down:
                table[i][j]=s[c]
                i+=1
                if i==numRows:
                    i-=2
                    j+=1
                    down=0
            else:
                table[i][j]=s[c]
                i-=1
                j+=1
                if i==0:
                    down=1
            c+=1
        ans=""
        for i in table:
            ans+="".join(i)
        return ans