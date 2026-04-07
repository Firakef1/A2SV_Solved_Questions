class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix)-1

        while left <= right:
            row = (left + right) // 2

            if target > matrix[row][-1]:
                left = row + 1

            elif target < matrix[row][0]:
                right = row - 1

            else:
                break

        else:
            return False
        
        arr = matrix[(left+right)//2]
        left = 0
        right = len(arr)-1
        print(arr)

        while left <= right:
            mid = (left+right)//2
            middle = arr[mid]

            # print(middle, target)
            if middle == target:
                return True
            elif target < middle:
                right = mid-1
            else:
                left = mid+1
            
        return False