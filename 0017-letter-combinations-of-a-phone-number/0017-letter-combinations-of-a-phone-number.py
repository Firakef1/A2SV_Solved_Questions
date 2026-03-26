class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        buttons = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        out = []

        def find(index, _len,  arr=[]):
            
            if len(arr) == _len:
                nonlocal out
                out.append("".join(arr))
                return
            
            nonlocal digits, buttons
            elem = digits[index]

            for i in buttons[int(elem)]:
                find(index+1, _len, arr+[i])
        
        find(0, len(digits))

        return out