class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = deque()
        new = [0]*len(temperatures)
        for i, n in enumerate(temperatures):
            # print(stack)
            if stack:
                while stack and stack[-1][0] < n:
                    elem = stack.pop()
                    # print(i-elem[1])
                    new[elem[1]] = i-elem[1]
                
                stack.append([n, i])
            else:
                stack.append([n, i])
        
        return new