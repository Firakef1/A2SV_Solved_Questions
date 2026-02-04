class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]

        for word in strs[1:]:
            i = 0

            while i < len(base) and i < len(word):
                if base[i] != word[i]:
                    base = base[:i]
                    break

                i += 1
            else:
                base = base if len(base) <= len(word) else word
        print(base)
        return base