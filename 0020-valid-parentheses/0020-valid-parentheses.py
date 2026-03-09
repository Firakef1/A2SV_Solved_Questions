class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in s:
            if i in "([{":
                stack.append(i)
            elif stack and stack[-1] == "(" and i == ")":
                stack.pop()
            elif stack and stack[-1] == "[" and i == "]":
                stack.pop()
            elif stack and stack[-1] == "{" and i == "}":
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        
        return True