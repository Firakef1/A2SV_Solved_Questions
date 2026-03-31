class Solution:
    def mySqrt(self, x: int) -> int:
        

        start, end = 1, x
        mid = 0
        while start <= end:
            mid = (start+end)//2

            val = mid*mid

            if val == x:
                return mid
            if val > x:
                end = mid-1
            else:
                start = mid+1
        
        return end