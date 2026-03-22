class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        place_holder= 0

        for seaker in range(len(nums)):

            if nums[seaker] != 0:

                nums[place_holder], nums[seaker] = nums[seaker], nums[place_holder]
                place_holder+=1






        