class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for i in edges:
            one = i[0]
            two = i[1]

            graph[one].append(two)
            graph[two].append(one)
        
        print(graph)
        
        def dfs(node, target, visted=set()):

            if node == target:
                return True
            
            visted.add(node)

            for i in graph[node]:
                if i not in visted:
                    if dfs(i, target, visted):
                        return True
            
            return False
            
        
        return dfs(source, destination)
        