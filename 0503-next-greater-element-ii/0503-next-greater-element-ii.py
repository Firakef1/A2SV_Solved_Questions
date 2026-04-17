class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double = nums*2
        
        stack = deque()
        out = []

        for i in range(len(double)-1, -1 , -1):
            
            while stack and stack[-1] <= double[i]:
                stack.pop()
            
            out.append(stack[-1] if stack else -1)
            # print(stack, "one")
            stack.append(double[i])
            # print(stack, "two")
        
        
        return out[::-1][:len(nums)]