class Solution:
    def decodeString(self, s: str) -> str:

        def find(index=0):
            string = ""
            num = ""
            i = index
            
            while i < len(s):
                char = s[i]
                
                if char.isdigit():
                    num += char
                elif char == "[":
                    inner_str, last_index = find(i + 1)
                    string += int(num) * inner_str
                    i = last_index
                    num = ""
                elif char == "]":
                    return string, i
                else:
                    string += char
                
                i += 1
                
            return string

        return find()