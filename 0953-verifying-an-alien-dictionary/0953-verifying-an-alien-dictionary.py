class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        data={}
        for i in range(26):
            data[order[i]]=i
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            j,k=0,0
            l1,l2=len(w1),len(w2)
            while j<l1 and k<l2:
                if data[w1[j]]>data[w2[k]]:
                    return 0
                elif data[w1[j]]<data[w2[k]]:
                    break
                j+=1
                k+=1
            if j<l1 and k==l2:
                return 0
        return 1