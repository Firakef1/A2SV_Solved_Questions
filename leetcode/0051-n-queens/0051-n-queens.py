class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        pos = set()
        neg = set()

        cur = [["."]*n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy  = ["".join(row) for row in cur]
                # print(copy)
                res.append(copy)
                return

            for c in range(n):

                if c in col or (c-r) in neg or (c+r) in pos:
                    continue


                col.add(c)
                pos.add(c+r)
                neg.add(c-r)
                cur[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                pos.remove(c+r)
                neg.remove(c-r)
                cur[r][c] = "."

        backtrack(0)

        return res                    