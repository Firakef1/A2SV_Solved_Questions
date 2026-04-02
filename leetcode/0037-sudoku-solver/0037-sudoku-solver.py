class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        col_line = {}
        row_line = {}

        for i in range(9):
            col_line[i] = set()
            row_line[i] = set()

        box = {}
        for i in range(3):
            for j in range(3):
                box[(i, j)] = set()
        
        for i, n in enumerate(board):
            for j, m in enumerate(n):
                if m != ".":

                    row_line[i].add(int(m))
                    col_line[j].add(int(m))
                    box[(i//3, j//3)].add(int(m))

        def back_track(row=0, col=0):
            if row == 9:
                return True
            
            next_row = row + (col + 1) // 9
            next_col = (col + 1) % 9

            if board[row][col] != ".":
                return back_track(next_row, next_col)

            for val in range(1, 10):              
                if val in row_line[row] or val in col_line[col] or val in box[(row//3, col//3)]:
                    continue

                
                row_line[row].add(val)
                col_line[col].add(val)
                box[(row//3, col//3)].add(val)
                board[row][col] = str(val)

                if back_track(next_row, next_col):
                    return True
                
                row_line[row].remove(val)
                col_line[col].remove(val)
                box[(row//3, col//3)].remove(val)
                board[row][col] = "."
            
            return False
        
        back_track()