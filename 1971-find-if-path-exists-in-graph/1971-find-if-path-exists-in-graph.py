class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for i in edges:
            one = i[0]
            two = i[1]

            graph[one].append(two)
            graph[two].append(one)
        
        stack = deque([source])
        visted = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            for elem in graph[node]:
                if elem not in visted:
                    visted.add(elem)
                    stack.append(elem)
        
        return False
            