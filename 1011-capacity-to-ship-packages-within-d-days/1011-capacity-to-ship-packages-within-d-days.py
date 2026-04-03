from bisect import bisect_left
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def find(capacity):
            count = 0
            cur = 0
            for i in weights:
                if cur + i <= capacity:
                    cur += i
                else:
                    cur = i
                    count +=1
            
            if cur > 0:
                count += 1
            
            if count <= days:
                return True
            
            return False

        right = sum(weights)
        left = max(weights)

        while left <= right:
            mid = (left+right)//2
            # print(mid)
            if find(mid):
                right = mid-1
            else:
                left = mid+1
        
        return left