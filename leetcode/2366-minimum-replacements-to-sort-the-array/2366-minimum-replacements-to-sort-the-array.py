class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        bound = nums[-1]
        res = 0

        for num in reversed(nums[:-1]):
            count = (num + bound - 1) // bound
            res += count -1
            bound = num//count
        
        return res