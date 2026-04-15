class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = deque()

        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        
        stack = list(stack)

        return "".join(stack)