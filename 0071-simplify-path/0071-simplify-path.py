class Solution:
    def simplifyPath(self, path: str) -> str:

        
        new = path.split("/")
        stack = deque()
        for i in range(0,len(new)):
            elem = new[i]

            if elem == "..":
                if stack:
                    stack.pop()
            
            elif elem == "." or elem == "":
                continue
            
            else:
                stack.append(elem)
        
        ans = "/" + "/".join(stack)

        return ans


        
        