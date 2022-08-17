class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        data=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s=set()
        for i in words:
            temp=""
            for j in i:
                temp+=data[ord(j)-97]
            s.add(temp)
        return len(s)