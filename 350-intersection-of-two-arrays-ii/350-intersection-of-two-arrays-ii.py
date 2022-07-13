class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        ans = []
        visit = [0]*l1
        for i in range(l2):
            for j in range(l1):
                if visit[j]==0 and nums2[i]==nums1[j]:
                    visit[j]=1
                    ans.append(nums2[i])
                    break
        return ans