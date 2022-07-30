class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = collections.Counter()
        for i in words2:
            count |= collections.Counter(i)
        return [i for i in words1 if not count-Counter(i)]