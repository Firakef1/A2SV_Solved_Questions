class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # if n == 1:
        #     return 5
        # if n%2 == 1:
        #     return 5*self.countGoodNumbers(n-1)%(pow(10, 9) + 7)
        # else:
        #     return 4*self.countGoodNumbers(n-1)%(pow(10, 9) + 7)

        even = ceil(n/2)
        odd = n//2
        mod = pow(10, 9) + 7

        return pow(5, even, mod)*pow(4, odd, mod)%mod
    
