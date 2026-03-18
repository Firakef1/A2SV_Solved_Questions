class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        
        def solve(one, two, state, left, right):
            
            if left > right:
                return True if one >= two else False

            elem_one = nums[left]
            elem_two = nums[right]

            if state:
                first = solve(one+elem_one, two, not state, left+1, right)
                second = solve(one+elem_two, two, not state, left, right-1)

                return first or second
            else:
                
                first = solve(one, two+elem_one, not state, left+1, right)
                second = solve(one, two+elem_two, not state, left, right-1)

                

                return first and second
        
        return solve(0, 0, True, 0, len(nums)-1)
            
            
