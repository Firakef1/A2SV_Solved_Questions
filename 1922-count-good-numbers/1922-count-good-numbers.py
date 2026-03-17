class Solution:
    def countGoodNumbers(self, n: int) -> int:

        
        even = n//2 if n%2 == 0 else n//2 +1
        odd = n//2

        return pow(5, even, 1000000007)*pow(4, odd, 1000000007)%1000000007
        