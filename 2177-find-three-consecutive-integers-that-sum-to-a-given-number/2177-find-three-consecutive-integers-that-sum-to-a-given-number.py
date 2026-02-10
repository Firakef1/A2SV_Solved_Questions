class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 != 0:
            return []

        qutient = num//3

        return [qutient-1, qutient, qutient+1]
    