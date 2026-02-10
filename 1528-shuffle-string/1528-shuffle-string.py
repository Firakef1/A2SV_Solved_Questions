class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_str = [0]*len(s)
        
        for i in range(len(indices)):
            new_str[indices[i]] = s[i]

        return "".join(new_str)
        