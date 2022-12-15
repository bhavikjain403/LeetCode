class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = []
        for i in range(len(text1)+1):
            table.append([0]*(len(text2)+1))  
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    table[i][j]= 1 + table[i-1][j-1]
                else:
                    table[i][j]= max(table[i-1][j], table[i][j-1])
        return table[-1][-1]