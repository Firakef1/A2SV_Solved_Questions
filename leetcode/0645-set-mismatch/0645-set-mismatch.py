class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = max(nums)
        count = [0] * (n + 1)
        for num in nums:
            count[num] += 1
        
        missing, repeating = -1, -1
        for i in range(1, n + 1):
            if count[i] == 0:
                missing = i
            elif count[i] == 2:
                repeating = i
        
        if missing == -1:
            missing = n+1
        
        return [repeating, missing]