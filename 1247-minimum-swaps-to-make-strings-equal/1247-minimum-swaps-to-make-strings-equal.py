class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        seen = defaultdict(int)

        x = s1.count("x") + s2.count("x")
        y = s1.count("y") + s2.count("y")

        if x%2 != 0 or y%2 != 0:
            return -1

        i = 0
        count = 0
        while i < len(s1):
            if s1[i] == s2[i]:
                i += 1
                continue

            arr = (s1[i], s2[i])

            seen[arr] += 1

            if seen[arr]%2 == 1:
                count += 1
            
            
            i += 1
        
        return count