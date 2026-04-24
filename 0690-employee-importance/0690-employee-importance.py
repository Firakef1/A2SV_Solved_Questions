"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        map_lis = defaultdict()

        for node in employees:
            map_lis[node.id] = node
        
        
        out = 0
        vistead = set()

        def dfs(node):
            nonlocal vistead, out, map_lis
            
            if node in vistead:
                return
            
            # print(node.importance)
            out += node.importance

            for i in node.subordinates:
                dfs(map_lis[i])
        
        for node in employees:
            
            if node.id == id:
                dfs(node)
        
        return out

            