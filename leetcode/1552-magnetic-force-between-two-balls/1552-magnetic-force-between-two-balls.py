class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def place(gap):
            
            count = 1
            prev = position[0]

            for i in position:
                if i-prev >= gap:
                    count += 1
                    prev = i
            
            return count >= m


        

        left, right = 1, max(position)
        ans = -1
        while left <= right:
            mid = (left + right)//2
  
            if place(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans