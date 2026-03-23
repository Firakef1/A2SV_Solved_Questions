class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        #increasing
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                break
        else:
            return True
        
        #desending
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                break
        else:
            return True

        return False
