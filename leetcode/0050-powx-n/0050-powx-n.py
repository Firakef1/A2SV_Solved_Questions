from math import pow
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(n, x):

            if n == 1:
                return x
            if n == 0:
                return 1
            cur = solve(n//2, x)

            return cur*cur if n%2 == 0 else x*cur*cur

        val = solve(abs(n), x)

        return val if n >= 0 else 1/val


        



        