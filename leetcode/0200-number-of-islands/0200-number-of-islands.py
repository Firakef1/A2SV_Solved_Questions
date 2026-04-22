class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        max_row, max_col = len(grid), len(grid[0])
        seen = [[False]*max_col for _ in range(max_row)]
        # print(seen)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def is_inbound(row, col, max_row, max_col):
            if row < max_row and row >= 0 and col < max_col and col >= 0:
                return True
            
            return False
        
        def find_iland(row, col):
            nonlocal seen, max_row, max_col, directions
            if seen[row][col] or grid[row][col] == "0":
                return
            
            seen[row][col] = True

            for direction in directions:
                cur_row = row + direction[0]
                cur_col = col + direction[1]

                if is_inbound(cur_row, cur_col, max_row, max_col):
                    print(cur_row, cur_col)
                    find_iland(cur_row, cur_col)
        
        count = 0

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == "1" and not seen[i][j]:
                    # print(i, j)
                    find_iland(i, j)
                    count += 1
        
        print(seen)
        return count