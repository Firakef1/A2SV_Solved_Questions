class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lis = list(range(1, n+1))
        final_count = 1
        
        i = -1
        while final_count < n:
            cur_count = 0
            while cur_count < k:
                i+=1
                if i == n:
                    i = i%n
                
                if lis[i] > 0:
                    cur_count += 1
                
                
                
            # print(i)
            lis[i] = -1
            final_count += 1
        
        # print(lis)
        for i in lis:
            if i > 0:
                return i
                