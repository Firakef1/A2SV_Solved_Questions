class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = [x for x in range(1, n + 1)]
        nums = []
        def combination(lst, i, curr):
            nonlocal nums
            if len(curr) == k:
                nums.append(curr)
                return 
            if i == len(arr):
                return

      
            combination(lst, i + 1, curr + [lst[i]])

            combination(lst, i + 1, curr)
            


        combination(arr, 0, [])
    
        return nums