class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="-":
                n1=stack.pop()
                n2=stack.pop()
                stack.append(n2-n1)
            elif i=="*":
                stack.append(stack.pop()*stack.pop())
            elif i=="/":
                n1=stack.pop()
                n2=stack.pop()
                if (n1>0 and n2<0) or (n1<0 and n2>0):
                    if abs(n2)%abs(n1)==0:
                        stack.append(n2//n1)
                    else:
                        stack.append(n2//n1+1)
                else:
                    stack.append(n2//n1)
            else:
                stack.append(int(i))
        return stack[0]