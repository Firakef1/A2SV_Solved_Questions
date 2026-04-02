class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def find(first, second, index):
            
            if index == len(num):
                return True
            val = 0
            for i in range(index+1, len(num)+1):
                val = num[index:i]
                # print(val)
                if val.startswith('0') and len(val) > 1:
                    break
                val = int(val)
                if val == first+second:
                    if find(second, val, i):
                        return True
            # print(val, "fianl")
            return False
            
        for i in range(1, len(num)):
            
            val_one = num[:i]

            if val_one.startswith('0') and len(val_one) > 1:
                    break
            val_one = int(val_one)

            for j in range(i+1, len(num)):
                
                val_two = num[i:j]

                if val_two.startswith('0') and len(val_two) > 1:
                    break
                
                val_two = int(val_two)
                # print(val_one, val_two)
                if find(val_one, val_two, j):
                    return True
        
        return False