class MyStack:

    def __init__(self):
        self.stack=[]
        self.l=0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.l+=1

    def pop(self) -> int:
        self.l-=1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if self.l>0:
            return 0
        return 1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()