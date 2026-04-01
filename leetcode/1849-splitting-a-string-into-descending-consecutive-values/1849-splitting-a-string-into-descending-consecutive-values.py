class Solution:
    def splitString(self, s: str) -> bool:
        
        def find(index, prev):

            if index == len(s):
                return True

            out = False
            for i in range(index, len(s)):
                val = int(s[index:i+1])

                if prev-val == 1:
                    if find(i+1, val):
                        return True

            return False
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if find(i+1, val): return True
        
        return False

            