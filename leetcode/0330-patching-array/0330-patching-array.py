class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        _sum = 0
        index = 0
        count = 0
        i = 0
        while i <= n:
            
            if _sum >= n:
                break
            if index < len(nums) and nums[index] <= _sum:
                _sum+=nums[index]
                index+=1
                # print(i, "zero")
            elif index < len(nums) and nums[index] == i:
                _sum += i
                index+= 1
                # print(i, "one")
            elif index < len(nums) and nums[index] > i and i > _sum:
                _sum += i
                count += 1
                # print(i, "two")
            elif i > _sum and index >= len(nums):
                _sum += i
                count += 1
                i = _sum
                # print(i, "three")
        # print(_sum)
            i+=1
        return count
