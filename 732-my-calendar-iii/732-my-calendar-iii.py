class MyCalendarThree:

    def __init__(self):
        self.pos = []
        self.delta = {}
        self.max = 0

    def book(self, start, end):
        i = bisect.bisect_left(self.pos, start)
        if start not in self.delta:
            self.delta[start] = self.delta[self.pos[i-1]] if i else 0
            self.pos[i:i] = [start]

        j = bisect.bisect_left(self.pos, end)
        if end not in self.delta:
            self.delta[end] = self.delta[self.pos[j-1]]
            self.pos[j:j] = [end]
        for k in range(i, j):
            self.delta[self.pos[k]] = c = self.delta[self.pos[k]] + 1
            self.max = max(self.max, c)
        return self.max
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)