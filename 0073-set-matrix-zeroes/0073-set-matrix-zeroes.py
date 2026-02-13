class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_index = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    zero_index.append([i, j])
        
        for i, j in zero_index:
            #set row
            for x in range(len(matrix[0])):
                matrix[i][x] = 0

            #set col
            for x in range(len(matrix)):
                matrix[x][j] = 0

        