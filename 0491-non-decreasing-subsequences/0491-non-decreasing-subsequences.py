class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        out = []

        def find(start, lis):
            if len(lis) > 1:
                if lis not in out:
                    out.append(lis[:])
            
            for i in range(start, len(nums)):
                val = nums[i]

                if val >= lis[-1]:
                    lis.append(val)
                    find(i+1, lis)
                    lis.pop()

        for i, n in enumerate(nums):
            find(i+1, [n])
        
        return out
