class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        _max = deque()

        for i in range(k):
            
            while _max and _max[-1] < nums[i]:
                _max.pop()
            
            _max.append(nums[i])
        
        left = 0
        right = k

        res = [_max[0]]

        while right< len(nums):

            #remove from the front
            if _max[0] == nums[left]:
                _max.popleft()
            
            #add to _max
            while _max and _max[-1] < nums[right]:
                _max.pop()
            else:
                _max.append(nums[right])
            
            right += 1
            left += 1
        
             #out here
            res.append(_max[0])
        
        # res.append(_max[0])
        
        return res
            

