class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        new_arr = [nums[0]]*len(nums)

        for i in range(1, len(nums)):
            new_arr[i] = new_arr[i-1]+ nums[i]

        return new_arr
        