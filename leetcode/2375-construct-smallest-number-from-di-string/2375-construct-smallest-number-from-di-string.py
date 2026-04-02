class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        seen = set()
        _min = float("inf")

        def backtrack(index, number=[]):
            nonlocal _min, seen
            if len(number) == len(pattern)+1:
                _min = min(_min, int("".join(number)))
                return
            
            if pattern[index] == "D":
                start = 1
                end = int(number[-1])
            else:
                start = int(number[-1])+1
                end = 10

            for i in range(start, end):
                if i in seen:
                    continue
                
                number.append(str(i))
                seen.add(i)
                backtrack(index+1, number)
                number.pop()
                seen.remove(i)
            
        
        for i in range(1, 10):
            seen.add(i)
            backtrack(0, [str(i)])
            seen.remove(i)
        
        return str(_min)