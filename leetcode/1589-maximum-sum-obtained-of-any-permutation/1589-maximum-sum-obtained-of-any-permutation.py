class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        range_sum = [0]*(len(nums)+1)

        for req in requests:
            range_sum[req[0]] += 1
            range_sum[req[1]+1] -= 1
    
        for i in range(1, len(range_sum)):
            range_sum[i] += range_sum[i-1]
        
        range_sum.sort()
        nums.sort()
        out = 0

        i = 0

        while i < len(nums):
            out += range_sum[i+1]*nums[i]
            i+=1
        
        return pow(out, 1, pow(10, 9)+7)