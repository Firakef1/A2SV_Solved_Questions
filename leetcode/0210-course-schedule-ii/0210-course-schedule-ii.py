class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        out = []
        graph = defaultdict(list)
        value = defaultdict(int)
        

        for node in prerequisites:
            graph[node[1]].append(node[0])
            value[node[0]] += 1
            value[node[1]] += 0
        

        queue = deque([i for i in range(numCourses) if value[i] == 0])

        while len(out) < numCourses:

            if not queue:
                return []

            val = queue.popleft()
            out.append(val)

            for i in graph[val]:
                value[i]-=1
                if value[i] == 0:
                    queue.append(i)

            
        return out
        

