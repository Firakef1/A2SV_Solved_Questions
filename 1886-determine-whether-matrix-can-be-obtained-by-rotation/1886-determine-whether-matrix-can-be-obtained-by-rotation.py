class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        new_mat = [[0]*n for _ in range(n)]
        for _ in range(4):

            for i in range(n):
                for j in range(n):
                    new_j = n - i - 1

                    new_mat[i][j] = mat[j][new_j]

            
            if new_mat == target:
                return True
            
            mat = new_mat
            new_mat = [[0]*n for _ in range(n)]

        return False