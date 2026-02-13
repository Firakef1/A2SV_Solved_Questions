class Solution:
    def intToRoman(self, num: int) -> str:
        roman_num_map = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 900:"CM", 400:"CD", 90:"XC", 40:"XL", 9:"IX", 4:"IV"}
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_number = ""
        modulo = num

        for number in numbers:
            quotient = modulo//number
            modulo = modulo%number

            letter = roman_num_map[number]
            roman_number += letter*quotient

        return roman_number
