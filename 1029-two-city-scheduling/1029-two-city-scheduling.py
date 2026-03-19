class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort( key=lambda x: x[0] -x[1])
        total = 0
        n = len(costs)
        print(costs)
        for i in range(n//2):

            total += costs[i][0] + costs[n-i-1][1]
        
        return total