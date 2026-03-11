class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        binary = bin(n)[2:]
        new = ""
        for i in binary:
            if i == "0":
                new += "1"
            else:
                new += "0"
        
        return int(new, 2)

        