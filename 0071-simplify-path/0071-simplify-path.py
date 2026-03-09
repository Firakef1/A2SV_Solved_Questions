class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = deque()
        for i in range(0,len(path)):
            elem = path[i]
            if elem == "..":
                if stack:
                    stack.pop()
            elif elem == "." or elem == "":
                continue
            else:
                stack.append(elem)
        return  "/" + "/".join(stack)


        
        