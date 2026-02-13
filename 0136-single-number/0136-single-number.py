class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = nums[0]

        for i in nums[1:]:
            number = number^i

        return number