class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        count_s = 0
        count_t = 0

        for i in s:
            count_s += ord(i)
        
        for i in t:
            count_t += ord(i)
        
        
        return chr(count_t-count_s)