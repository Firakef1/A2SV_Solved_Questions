class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        num_dict = defaultdict(int)
        total = 0
        count = 0

        for i in nums:
            total += i

            if total == goal:
                count += 1
            
            if total-goal in num_dict:
                count += num_dict[total-goal]
            
            num_dict[total] += 1
        
        return count