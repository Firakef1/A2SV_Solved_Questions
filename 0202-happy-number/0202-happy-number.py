class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        one = n
        two = 0

        while one not in seen:
            if one == 1:
                return True

            for i in str(one):
                two += int(i)**2
            seen.add(int(one))
            one = two
            two = 0

        return False