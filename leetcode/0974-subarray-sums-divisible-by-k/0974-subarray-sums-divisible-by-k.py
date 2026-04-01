class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = {0: 1}  
        count = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            
            remainder = prefix_sum % k
            
            
            if remainder in table:
                count += table[remainder]
            
            table[remainder] = table.get(remainder, 0) + 1
        
        return count