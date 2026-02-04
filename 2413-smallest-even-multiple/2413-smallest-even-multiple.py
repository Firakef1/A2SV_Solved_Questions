class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        number = n

        while True:
            if number%2 == 0 and number%n == 0:
                return number
            number += n

        


        