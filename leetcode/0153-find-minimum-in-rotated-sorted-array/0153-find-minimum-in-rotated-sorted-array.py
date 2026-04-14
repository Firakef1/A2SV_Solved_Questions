class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find(left, right):
            
            if right-left <= 1 and right >= left:
                return min(nums[right], nums[left])
            
            mid = (left+right)//2

            one = find(left, mid)
            two = find(mid+1, right)

            return min(one, two)

        return find(0, len(nums)-1)