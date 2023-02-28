class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2=len(nums1),len(nums2)
        ans=[-1]*n1
        for i in range(n1):
            flag=0
            for j in range(n2):
                if flag==1 and nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
                if nums1[i]==nums2[j]:
                    flag=1
        return ans