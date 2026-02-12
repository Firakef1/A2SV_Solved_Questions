class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        cur = 0
        seen = set()

        for i in nums:
            
            cur = 1
            temp = i
            if i in seen:
                continue
            
            while temp-1 in set_nums:
                temp = temp-1
                seen.add(temp)
            
            while temp+1 in set_nums:
                cur += 1
                temp += 1
                seen.add(temp)

            max_count = max(cur, max_count)
            

        return max_count


            