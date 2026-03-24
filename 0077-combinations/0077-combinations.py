class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = [x for x in range(1, n + 1)]
        nums = []
        def combination(lst, i, curr):
            nonlocal nums
            if i == len(arr):
                nums.append(curr)
                return 
            

      
            combination(lst, i + 1, curr + [lst[i]])

            combination(lst, i + 1, curr)
            


        combination(arr, 0, [])
        ans = [x for x in nums if len(x) == k]
        return ans