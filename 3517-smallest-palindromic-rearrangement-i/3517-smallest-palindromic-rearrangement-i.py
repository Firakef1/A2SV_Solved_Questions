class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        left = ""
        right = ""
        middle = ""

        for i in count:
            if count[i]%2 == 1:
                middle = i
                count[i]-=1
        
        order = sorted(list(set(s)))

        for i in order:
            while count[i] > 0:
                left += i
                right = i + right
                count[i] -= 2

        return left+middle+right
