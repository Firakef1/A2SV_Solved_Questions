class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        one = nums[0]
        two = nums[1]
        three = nums[2]

        i = 0

        while i < len(nums)-2:

            if three + two > one:
                return one+two+three

            one = nums[i]
            two = nums[i+1]
            three = nums[i+2]

            i += 1
        
        if three + two > one:
            return one+two+three
        return 0
    
    #3 3 2