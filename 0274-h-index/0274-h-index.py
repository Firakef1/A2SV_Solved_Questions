class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        max_h = 0
        cur = 0
        for i, n in enumerate(citations):
            cur = min(i+1, n)
            max_h = max(cur, max_h)

        return max_h