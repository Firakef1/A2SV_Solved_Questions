class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = deque()
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                temp = 0
                while stack[-1] != 0:
                    temp += stack.pop()
    
                stack.pop()
                stack.append(2*temp if temp else 1)
        
        return sum(stack)
        