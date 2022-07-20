class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count=0
        for i in words:
            flag=1
            cpy=s
            for j in i:
                if j in cpy:
                    cpy=cpy[cpy.index(j)+1:]
                else:
                    flag=0
                    break
            if flag:
                count+=1
        return count