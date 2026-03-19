from math import ceil
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        total = 0

        while maxDoubles and target//2 >= 1:

            if target%2 == 1:
                target -= 1
                total += 1
            target/=2
            total += 1
            maxDoubles-= 1
        
        total += int(target) - 1
        return total