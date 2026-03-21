class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        one = 0
        out = ""

        while one < len(word1) and one < len(word2):
            out += word1[one]
            out += word2[one]

            one += 1
        
        out += word1[one:]+word2[one:]

        return out