class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def is_valid(lis):
            stack = deque()

            for i, n in enumerate(lis):
                if lis[i] not in "()":
                    continue
                
                if n == "(":
                    stack.append(["(", i])
                elif n ==")" and stack:
                    stack.pop()
                else:
                    return False
            if stack:
                return False
            
            return True
        
        def find(lis, index=0):
            nonlocal len_out, out

            if len(lis) < len_out or len(lis)  < 1:
                return
            
            if is_valid(lis):

                sol = "".join(lis)
                if len(lis) > len_out:
                    out = [sol]
                    len_out = len(lis)
                if len(lis) == len_out:
                    if sol not in out:
                        out.append(sol)
            
            for i in range(index, len(lis)):
                if lis[i] == "(" or lis[i] == ")":
                    find(lis[:i]+lis[i+1:], i)
        

        lis = [x for x in s]
        out = []
        len_out = 0

        find(lis)
        return out if out else [""]



