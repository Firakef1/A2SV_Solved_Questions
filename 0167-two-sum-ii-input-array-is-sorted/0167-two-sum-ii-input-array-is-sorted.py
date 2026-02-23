class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0,len(numbers)-1

        while left < right:
            one = numbers[left]
            two = numbers[right]
            
            if one+two == target:
                return [left+1, right+1]
            elif one+two < target:
                left += 1
            else:
                right -= 1

        