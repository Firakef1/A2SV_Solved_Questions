class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        val = None

        for i in s:
            if int(i) == count[i]:
                if val and val != i:
                    return val+i
                val = i
            else:
                val = None
        
        return ""