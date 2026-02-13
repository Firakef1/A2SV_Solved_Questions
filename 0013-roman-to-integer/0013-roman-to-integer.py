class Solution:
    def romanToInt(self, s: str) -> int:
            num_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "CM":900, "CD":400, "XC":90, "XL":40, "IX":9, "IV":4}
            num = 0

            one, two = 0, 1

            while one < len(s):
                if two < len(s) and num_map[s[one]] < num_map[s[two]]:
                    num += num_map[s[one]+s[two]]
                    one += 2
                    two += 2
                else:
                    num += num_map[s[one]]
                    one += 1
                    two += 1

            
            return num