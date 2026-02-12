class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted(s, key=lambda x:(-s.count(x), x) )
        return "".join(s)