class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            if pow(left, 2) + pow(right, 2) == c:
                return True
            
            elif pow(left,2) + pow(right, 2) > c:
                right -= 1
            
            else:
                left += 1

        return False
