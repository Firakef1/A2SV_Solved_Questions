class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
      
        nums.sort()


        for i in range(len(nums)-1, 1, -1):

            one, two, three = nums[i], nums[i-1], nums[i-2]

            if two+three > one:
                return one + two +three
        
        return 0
