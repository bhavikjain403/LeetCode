from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.data=SortedList()
        self.l=0

    def addNum(self, num: int) -> None:
        self.data.add(num)
        self.l+=1

    def findMedian(self) -> float:
        if self.l==0:
            return 0
        if self.l%2:
            return self.data[self.l//2]
        return (self.data[self.l//2-1]+self.data[self.l//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()