class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        graph = defaultdict(list)

        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        
        seen = set()
        def dfs(node):
            nonlocal graph, seen

            if not graph[node]:
                return
            
            if node == destination:
                return True
            ans = False
            for i in graph[node]:
                if i not in seen:
                    seen.add(node)
                    ans = ans or dfs(i)
            
            return ans
        
        return dfs(source)