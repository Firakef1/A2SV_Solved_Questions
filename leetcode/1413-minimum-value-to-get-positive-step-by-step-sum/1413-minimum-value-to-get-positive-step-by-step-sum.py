class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]

        for i in nums:
            prefix.append(prefix[-1]+i)

        _min = 1-min(prefix)

        return _min if _min > 0 else 1