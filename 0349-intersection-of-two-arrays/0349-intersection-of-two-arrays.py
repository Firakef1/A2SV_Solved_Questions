class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_one = Counter(nums1)
        new_arr = []

        for i in nums2:
            if i in count_one and i not in new_arr:
                new_arr.append(i)

        return new_arr