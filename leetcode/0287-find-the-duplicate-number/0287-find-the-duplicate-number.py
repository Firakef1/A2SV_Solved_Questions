class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = max(nums)
        # return sum(nums) - n*(n+1)//2

        for i, n in enumerate(nums):
            if nums[abs(n)-1] < 0:
                return abs(n)
            else:
                nums[abs(n)-1] = -nums[abs(n)-1]
        