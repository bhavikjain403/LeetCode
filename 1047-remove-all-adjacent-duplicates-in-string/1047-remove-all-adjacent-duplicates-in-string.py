class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)           
        return "".join(stack)