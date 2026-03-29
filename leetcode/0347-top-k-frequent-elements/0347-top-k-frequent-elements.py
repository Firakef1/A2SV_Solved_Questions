class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        count = count.most_common()

        out = [count[i][0] for i in range(k)]

        return out
