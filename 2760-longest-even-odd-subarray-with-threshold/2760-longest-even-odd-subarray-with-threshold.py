class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        _max = 0
        left = 0

        for right in range(len(nums)):

  
            if nums[right] > threshold:
                left = right + 1
                continue

   
            if nums[left] % 2 != 0:
                left += 1
                continue

            if right > left and nums[right] % 2 == nums[right - 1] % 2:
                left = right

            _max = max(_max, right - left + 1)

        return _max


            