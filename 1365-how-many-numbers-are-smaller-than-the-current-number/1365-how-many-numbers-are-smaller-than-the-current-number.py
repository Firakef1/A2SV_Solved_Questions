class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        index_dict = {}
        for i, n in enumerate(sorted_nums):
            if n not in index_dict:
                index_dict[n] = i

        for i, n in enumerate(nums):
            sorted_nums[i] = index_dict[n]

        return sorted_nums 