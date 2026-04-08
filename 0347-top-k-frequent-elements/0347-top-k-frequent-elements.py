class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        freq = freq.most_common()
        
        return [freq[i][0] for i in range(k)]