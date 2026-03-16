class Solution:
    def fib(self, n: int, memo = {}) -> int:

        #base case
        if n in memo:
            return memo[n]
        
        #base case 
        if n <= 2:
            return 1 if n != 0 else 0
        
        #recurance relation and the step 
        memo[n] = self.fib(n-1, memo)+self.fib(n-2, memo)

        return memo[n]