from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heapify_max(piles)

        for _ in range(k):
            temp = heappop_max(piles)
            temp = ceil(temp/2)
            heappush_max(piles, temp)
        
        return sum(piles)