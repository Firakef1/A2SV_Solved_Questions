class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        first = sum(nums[:k])
        max_average = first

        i = k

        while i < len(nums):
            max_average = max(first, max_average)
            # print(first)
            first -= nums[i-k]
            first += nums[i]
            i += 1
        else:
            max_average = max(first, max_average)
        
        return max_average/k

