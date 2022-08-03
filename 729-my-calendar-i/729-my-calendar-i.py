class MyCalendar:

    def __init__(self):
        self.cal=[]

    def book(self, start: int, end: int) -> bool:
        l=len(self.cal)
        if l==0:
            self.cal.append([start,end])
            return True
        for i in range(l):
            if start>=self.cal[i][1] or end<=self.cal[i][0]:
                continue
            else:
                return False
        self.cal.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)