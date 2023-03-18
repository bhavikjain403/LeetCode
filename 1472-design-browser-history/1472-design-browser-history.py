class BrowserHistory:

    def __init__(self, homepage: str):
        self.a=[homepage]
        self.clear=0
        self.curr=0
        
    def visit(self, url: str) -> None:
        self.curr+=1
        if self.curr==len(self.a):
            self.a.append(url)
        else:
            self.a[self.curr]=url
        self.clear=self.curr

    def back(self, steps: int) -> str:
        self.curr=max(0,self.curr-steps)
        return self.a[self.curr]

    def forward(self, steps: int) -> str:
        self.curr=min(self.clear,self.curr+steps)
        return self.a[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)