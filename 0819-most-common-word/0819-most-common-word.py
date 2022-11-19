class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d = dict()
        for c in paragraph:
            if(c == '!' or c == ',' or c == '.' or c == '?' or c == ';' or c == "'"):
                paragraph = paragraph.replace(c, ' ')
        paragraph = paragraph.split()
        for word in paragraph:
            word = word.lower()
            if(word not in banned):
                if(word not in d):
                    d[word] = 1
                else:
                    d[word] += 1
        return max(d, key = d.get)