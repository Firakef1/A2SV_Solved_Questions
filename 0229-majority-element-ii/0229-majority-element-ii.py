class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        num = nums[0]
        freq= 1
        out = []
        for i in nums[1:]:
            if i == num:
                freq+= 1
            else:
                if freq > len(nums)/3:
                    out.append(num)
               
                num = i
                freq = 1
        
        if freq > len(nums)/3:
            out.append(num)

        return out