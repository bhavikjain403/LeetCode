class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for i in sorted(counter.keys()):
            while counter[i] > 0:
                last = 0
                j = i
                k = 0
                while counter[j] >= last:
                    last = counter[j]
                    counter[j] -= 1
                    j += 1
                    k += 1
                if k < 3:
                    return False
        return True