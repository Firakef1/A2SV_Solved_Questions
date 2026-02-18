class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        lis = []
        def solve(j, k, arr = []):
            # print(arr)
            # print(len(arr), k)
            
            if len(arr) == k:
                lis.append(arr[:])
                return
            
            for i in range(j,n+1):
                arr.append(i)
                solve(i+1, k, arr)
                arr.pop()
            
        solve(1, k)
        return lis