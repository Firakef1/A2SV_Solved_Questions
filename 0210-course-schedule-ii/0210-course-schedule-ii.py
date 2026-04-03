class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        out = []
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        
        for node in prerequisites:
            graph[node[1]].append(node[0])
            inDegree[node[0]] += 1
            inDegree[node[1]] += 0

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        while queue:

            val = queue.popleft()
            out.append(val)

            for i in graph[val]:
                inDegree[i]-=1
                if inDegree[i] == 0:
                    queue.append(i)

            
        if len(out) == numCourses:
            return out
        
        return []
        

