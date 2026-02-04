class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        new_arr = []

        for i, j in ranges:
            new_arr.extend(list(range(i, j+1)))

        for i in range(left, right+1):
            if i not in new_arr:
                return False

        return True

            
        