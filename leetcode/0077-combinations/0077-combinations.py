class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = []

        def find(j, k, nums=[]):

            if len(nums) == k:
                nonlocal arr
                arr.append(nums[:])
                return
            
            for i in range(j,n+1):
                nums.append(i)
                find(i+1, k, nums)
                nums.pop()
            
        find(1, k)

        return arr