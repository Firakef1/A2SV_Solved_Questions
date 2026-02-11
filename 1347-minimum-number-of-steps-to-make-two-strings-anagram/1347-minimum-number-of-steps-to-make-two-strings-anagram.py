class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        min_change = 0

        for key in count_s:
            if key in count_t:
                if count_s[key] > count_t[key]:
                    min_change += count_s[key] - count_t[key]
            else:
                min_change += count_s[key]

        return min_change