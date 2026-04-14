class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def find(val):
            count = 0

            for i in candies:
                count += i//val
            # print(count)
            return count >= k

        
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)
        ans = 1
        while left <= right:
            mid = (left + right)//2

            if find(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans
