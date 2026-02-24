class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        longest = ""

        for word in dictionary:

            if not set(word) <= set(s):
                continue
            
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            if j != len(word):
                continue
            
            if len(word) == len(longest):
                longest = min(longest, word)
            
            elif len(word) > len(longest):
                longest = word

        return longest