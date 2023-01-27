class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s=set(words)
        ans=[]
        for word in words:
            if word!="":
                stack=[0]
                seen=set()
                n=len(word)
                while stack:
                    w=stack.pop()
                    if w==n:
                        ans.append(word)
                        break
                    for i in range(n-w+1):
                        if word[w:w+i] in s and w+i not in seen and (w>0 or w+i!=n):
                            stack.append(w+i)
                            seen.add(w+i)
        return ans