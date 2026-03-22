class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = [str(x) for x in digits]
        
        num = int("".join(digits))+1
        num = [int(x) for x in str(num)]

        return num