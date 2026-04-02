class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        out = []

        def backtrack(start, words=[]):
            
            if start >= len(s):
                out.append(" ".join(words))
                return
            
            for i in range(start+1, len(s)+1):
                word = s[start:i]
                # print(word)
                if word in wordDict:
                    words.append(word)
                    backtrack(i, words)
                    words.pop()

        backtrack(0)

        return out
            