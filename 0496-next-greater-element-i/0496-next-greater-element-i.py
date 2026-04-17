class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        val_dict = defaultdict()

        stack = deque()

        for i in range(len(nums2)-1, -1, -1):
            
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            val_dict[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        out = []

        for i in nums1:
            out.append(val_dict[i])
        
        return out
