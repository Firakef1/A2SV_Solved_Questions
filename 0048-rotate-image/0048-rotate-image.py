class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        swapped = set() #set
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if (i, j) in swapped:
                    continue
                
                inverse_i = n-j-1
                inverse_j = n-i-1

                #swap
                matrix[i][j], matrix[inverse_i][inverse_j] = matrix[inverse_i][inverse_j], matrix[i][j]
                swapped.add((inverse_i, inverse_j))

        matrix.reverse()
                
        
