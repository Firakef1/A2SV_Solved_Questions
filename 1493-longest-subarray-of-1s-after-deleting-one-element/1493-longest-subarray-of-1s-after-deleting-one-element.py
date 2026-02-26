class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _max = 0
        left = right = 0
        found = False

        while right < len(nums):
            if nums[right] == 0 and found:

                _max = max(_max, right-left-1)

                while left < right and nums[left] != 0:
                    left += 1
                left += 1

                # if right < left:
                #     right = left

            elif nums[right] == 0:
                found = True
            

            right += 1

        _max = max(_max, right-left-1)
        # print(nums[left:right+1])
        return _max
            

            


        