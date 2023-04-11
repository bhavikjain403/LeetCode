class Solution:
    def removeStars(self, s: str) -> str:
        stack=deque()
        for i in s:
            if i!='*':
                stack.append(i)
            else:
                stack.pop()
        ans=""
        for i in stack:
            ans+=i
        return ans