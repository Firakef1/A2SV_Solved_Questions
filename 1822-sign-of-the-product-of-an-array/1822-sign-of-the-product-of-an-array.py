class Solution:
    def arraySign(self, nums: List[int]) -> int:

        if 0 in nums:
            return 0

        negative = sum(1 for i in nums if i < 0)

        if negative%2:
            return -1

        return 1
