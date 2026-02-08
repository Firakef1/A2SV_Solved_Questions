class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        total = sum(arr)

        prefix = [0]

        for i in arr:
            prefix.append(prefix[-1]+i)

        gap = 3

        while gap  <= len(arr):
            i = 0

            while i+gap < len(prefix):
                total += prefix[i+gap] - prefix[i]

                i += 1

            gap += 2

        return total
        