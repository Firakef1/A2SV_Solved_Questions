class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new_nums = sorted(nums)

        left, right = 0, len(nums)-1

        while left < right:

            number = new_nums[left]+new_nums[right]
            if number == target:
                if new_nums[left] == new_nums[right]:
                    index_one = nums.index(new_nums[left])
                    index_two = nums.index(new_nums[right], index_one+1)
                    return [index_one, index_two]

                return [nums.index(new_nums[left]), nums.index(new_nums[right])]

            elif number < target:
                left += 1
                
            else:
                right -= 1 

        return -1  