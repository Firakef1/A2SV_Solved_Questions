class Solution:
    def missingNumber(self, nums: List[int]) -> int:


        this_sum = sum(nums)
        n = max(nums)
        total_sum = (n*(n+1))/2

        return n+1 if int(total_sum - this_sum)==0  and 0 in nums else int(total_sum - this_sum)
 
        