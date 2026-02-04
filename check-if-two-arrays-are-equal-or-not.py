class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        
        if len(a) != len(b):
            return False
            
        i = 0
        a.sort()
        b.sort()
        while i < len(a):
            if a[i] != b[i]:
                return False
                
            i += 1
                
        return True