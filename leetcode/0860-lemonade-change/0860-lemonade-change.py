class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count =  defaultdict(int)

        for i in bills:
            count[i] += 1

            if i == 10:
                if not count[5]:
                    return False
                
                count[5]-=1
            
            if i == 20:
                if not count[10] and count[5] < 3 or count[10] and not count[5]:
                    return False

                if count[10]:
                    count[10]-=1
                    count[5]-=1
                else:
                    count[5]-=3

        return True 