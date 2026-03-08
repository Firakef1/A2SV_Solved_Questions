class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if len(stack) and (
                    (i == ")" and stack[-1] == "(")
                    or (i == "]" and stack[-1] == "[")
                    or (i == "}" and stack[-1] == "{")
                ):
                    stack.pop()
                    continue
                return False

        return False if len(stack) else True
