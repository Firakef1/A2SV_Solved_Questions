from heapq import heapify_max, heappop_max, heappush_max
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        half_sum = sum(nums)/2
        cur_sum = half_sum*2
        heapify_max(nums)
        count = 0
        while cur_sum > half_sum:
            count += 1
            temp = heappop_max(nums)
            temp /= 2
            cur_sum -= temp
            heappush_max(nums, temp)
        
        return count