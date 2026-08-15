class Solution:

    def bin(self, n:int) -> str:
        count = 0
        while n > 1:
            if n%2 == 1:
                count += 1
            n//= 2
        
        if n == 1:
            count += 1

        return count

    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            out.append(self.bin(i))
        
        return out

            
        
