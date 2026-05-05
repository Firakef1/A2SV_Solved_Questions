from heapq import heapify_max, heappop_max, heappush_max

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        heapify_max(gifts)

        for _ in range(k):
            temp = heappop_max(gifts)
            temp = floor(temp**0.5)
            heappush_max(gifts, temp)
        
        return sum(gifts)