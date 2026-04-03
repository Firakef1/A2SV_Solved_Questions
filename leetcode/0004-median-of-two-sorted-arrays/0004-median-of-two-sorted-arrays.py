class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1)+len(nums2)
        new = [0]*(total_len)
        one = two = 0

        while one < len(nums1) and two < len(nums2):
            val_one = nums1[one]
            val_two = nums2[two]

            if val_one < val_two:
                new[one+two] = val_one
                one += 1
            else:
                new[one+two] = val_two
                two += 1
        
        for i in range(one, len(nums1)):
            new[i+two] = nums1[i]
        for i in range(two, len(nums2)):
            new[i+one] = nums2[i]

        if total_len%2 == 1:
            return new[total_len//2]
        else:
            return (new[total_len//2-1] + new[total_len//2])/2