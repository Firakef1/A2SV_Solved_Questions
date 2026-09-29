class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort(reverse=True)

        one, two, three = nums[0], nums[1], nums[2]

        if two+three > one:
            return one+two+three
        

        return self.largestPerimeter(nums[1:])

        


