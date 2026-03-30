class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        negative_diagonal = set()
        positive_diagonal = set()

        total = []
        out = []

        def solve(row=0):
            if row == n:
                total.append(out[::])
                return
            
            line = ["."]*n

            for col in range(n):

                if col in cols or col+row in positive_diagonal or col-row in negative_diagonal:
                    continue
                
               
                line[col] = "Q"
                print(line)
                cols.add(col)
                positive_diagonal.add(col+row)
                negative_diagonal.add(col-row)

                out.append("".join(line))
                solve(row+1)

                out.pop()
                line[col] = "."

                cols.remove(col)
                positive_diagonal.remove(col+row)
                negative_diagonal.remove(col-row)

        solve()

        return len(total)
