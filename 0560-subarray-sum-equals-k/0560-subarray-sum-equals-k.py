class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sub_num = {0:1}
        total = count = 0
        count = 0

        for i in nums:
            total += i

            if total-k in sub_num:
                count += sub_num[total-k]
            
            if total in sub_num:
                sub_num[total] += 1
            else:
                sub_num[total] = 1
        
        return count