class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        strings = []

        def backtrack(string):
            # print(string)
            if len(string) == n:
                strings.append("".join(string))
                return
            
            for i in ["a", "b", "c"]:
                if i == string[-1]:
                    continue
                
                string.append(i)
                backtrack(string)
                # print(string, "ind")
                string.pop()
        
        for i in ["a", "b", "c"]:
            backtrack([i])
        
        strings.sort()

        if len( strings) >= k:
            return  strings[k-1]
        else:
            return ""
    