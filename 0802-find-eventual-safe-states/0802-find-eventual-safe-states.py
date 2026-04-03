class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        out = []
        
        color = defaultdict(int)

        def dfs(node):
            if color[node] == 1:
                return False
            
            if color[node] == 2:
                return True

            color[node] = 1

            for i in graph[node]:

                if not dfs(i):
                    return False
            
            color[node] = 2
            out.append(node)
            return True
         
        
        
        for i in range(len(graph)):
            if color[i] != 2:
                dfs(i)

        out.sort()

        return out