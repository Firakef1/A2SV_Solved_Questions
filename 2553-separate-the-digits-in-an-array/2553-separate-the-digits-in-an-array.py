class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return_arr = []

        for num in nums:
            for i in str(num):
                return_arr.append(int(i))

        return return_arr