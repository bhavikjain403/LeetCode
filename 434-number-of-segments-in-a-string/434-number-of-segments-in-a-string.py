class Solution:
    def countSegments(self, s: str) -> int:
        return sum([1 for i in s.split(" ") if i !=""])