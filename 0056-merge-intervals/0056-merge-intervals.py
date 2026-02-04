class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        final = []
        temp = intervals[0]

        for interval in intervals[1:]:
            if temp[1] >= interval[0]:
                temp[1] = max(interval[1], temp[1])
            else:
                final.append(temp)
                temp = interval

        final.append(temp)
        return final