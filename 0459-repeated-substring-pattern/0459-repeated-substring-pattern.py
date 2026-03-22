class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        substring = ""
        # last = s
        for i in range(len(s)//2):
            substring += s[i]
            if len(s)%(i+1) != 0:
                continue
            
            
            print(substring)
            # last = last[1:]
            
            count = len(s)//(i+1)

            if s.count(substring)*len(substring)==len(s):
                return True
        
        return False