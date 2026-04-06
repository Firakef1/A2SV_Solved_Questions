class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = set()

        def find(index, arr=[]):
            if index == len(nums):
                return

            for i in range(index, len(nums)):
                arr.append(nums[i])
                out.add(tuple(sorted(arr)))

                find(i+1, arr)
                arr.pop()
        
        for i in range(len(nums)):
            find(i)
        
        out = list(out)

        return [list(x) for x in out] + [[]]
       