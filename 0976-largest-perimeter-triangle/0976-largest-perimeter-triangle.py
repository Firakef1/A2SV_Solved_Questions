class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        nums = deque(nums)
       
        one = two = three = 0

        while True:
            if len(nums) < 3:
                break
            one = nums[-1]
            two = nums[-2]
            three = nums[-3]

            if two+three <= one:
                # print(nums)
                nums.pop()
            else:
                return one+two+three
        
        return 0

        

        
            