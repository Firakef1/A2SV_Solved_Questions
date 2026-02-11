class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_num1 = set(nums1)
        set_num2 = set(nums2)

        one = set_num1-set_num2
        two = set_num2-set_num1

        return [list(one), list(two)]