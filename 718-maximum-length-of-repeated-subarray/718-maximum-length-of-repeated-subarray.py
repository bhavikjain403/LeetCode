class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lcs = ""
        table = []
        for i in range(len(nums1)+1):
            table.append([0]*(len(nums2)+1))  
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    table[i][j]= 1 + table[i-1][j-1]
        return max(max(i) for i in table)