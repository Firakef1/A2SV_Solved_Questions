class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        state = False

        for i in nums:
            if i == 0:
                state = True
                continue

            total *= i
        
        if nums.count(0) > 1:
            total = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                nums[i] = total
                continue
            if state:
                nums[i] = 0
                continue

            nums[i] = total//n
        

        return nums