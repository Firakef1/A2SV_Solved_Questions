class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_dict = {}
        reverse_map = {}
        s = s.split()
        # print(s)
        i = 0

        while i < len(pattern) and i < len(s):
            # print(map_dict)

            if pattern[i] in map_dict and map_dict[pattern[i]] != s[i]:
                return False
            
            if s[i] in reverse_map and reverse_map[s[i]] != pattern[i]:
                return False
            
            reverse_map[s[i]] = pattern[i]
            map_dict[pattern[i]] = s[i]
            i+=1
        
        if i != len(pattern) or i != len(s):
            return False
        
        return True
        