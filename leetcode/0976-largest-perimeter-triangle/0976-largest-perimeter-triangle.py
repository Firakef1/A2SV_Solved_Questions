class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0

        while i < len(nums)-2:

            one = nums[i]
            two = nums[i+1]
            three = nums[i+2]

            if three + two > one:
                return one+two+three

            i += 1
        return 0
    
    #6 3 3 2