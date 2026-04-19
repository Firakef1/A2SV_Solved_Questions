class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        _max = 0
        for i in range(1, len(nums)):
            _max = max(nums[i]-nums[i-1], _max)
        
        return _max
        