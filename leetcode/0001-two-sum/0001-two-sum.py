class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        index_dict = defaultdict(list)

        for i, n in enumerate(nums):
            index_dict[n].append(i)
        
        nums.sort()

        left = 0
        right = len(nums)-1

        while left < right:
            tot = nums[left]+nums[right]
            if tot == target:
                return [index_dict[nums[left]].pop(), index_dict[nums[right]].pop()]

            elif tot < target:
                left += 1
            else:
                right -= 1
        
        return -1

        