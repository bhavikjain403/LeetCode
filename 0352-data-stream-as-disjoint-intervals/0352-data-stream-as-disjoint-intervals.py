class SummaryRanges:

    def __init__(self):
        self.starts, self.ends, self.used = [-float("inf"), float("inf")], [-float("inf"), float("inf")], set()

    def addNum(self, value: int) -> None:
        if value not in self.used:
            self.used.add(value)
            i = bisect.bisect_left(self.starts, value) - 1
            if self.ends[i] + 1 == value and value + 1 == self.starts[i + 1]:
                del self.starts[i + 1]
                del self.ends[i]
            elif self.ends[i] + 1 == value:
                self.ends[i] += 1
            elif self.starts[i + 1] == value + 1:
                self.starts[i + 1] -= 1
            elif value > self.ends[i]:
                self.starts.insert(i + 1, value) 
                self.ends.insert(i + 1, value)

    def getIntervals(self) -> List[List[int]]:
        return [[s, e] for s, e in zip(self.starts[1:-1], self.ends[1:-1])]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()