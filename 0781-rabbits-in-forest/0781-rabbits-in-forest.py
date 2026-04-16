from math import ceil
class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = Counter()
        total = 0
        for i in answers:
            if i == 0:
                total += 1
                continue 
            
            count[i]+=1
            if count[i] == 1:
                total += i+1
            elif count[i] == i+1:
                count[i] = 0
        
        return total