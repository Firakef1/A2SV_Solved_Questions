class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        # print(new_matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print(j, i)
                new_matrix[j][i] = matrix[i][j]
        
        return new_matrix