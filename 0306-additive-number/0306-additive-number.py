class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def isValid(s):
            if len(s) > 1 and s[0] == '0':
                return False
            return True

        def find(first, second, index):
            if index == n:
                return True
            
            for i in range(index + 1, n + 1):
                val_str = num[index:i]
                if not isValid(val_str):
                    continue
                
                val = int(val_str)

                if val == first + second:
                    return find(second, val, i)
                
                if val > first + second:
                    break
            
            return False

        for i in range(1, n):
            s1 = num[:i]
            if not isValid(s1): break 
            
            for j in range(i + 1, n):
                s2 = num[i:j]
                if not isValid(s2): break 
                
                if find(int(s1), int(s2), j):
                    return True
        
        return False