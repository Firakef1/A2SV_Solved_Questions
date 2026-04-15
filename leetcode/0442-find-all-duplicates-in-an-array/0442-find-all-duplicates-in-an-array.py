class Solution:
  
    def findDuplicates(self, nums: List[int]) -> List[int]:

        out = []

        for i in nums:
            if nums[abs(i)-1] != abs(nums[abs(i)-1]):
                out.append(abs(i))
            else:
                nums[abs(i)-1] = -nums[abs(i)-1]

        return out

        
