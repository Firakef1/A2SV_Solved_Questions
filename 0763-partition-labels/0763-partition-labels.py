class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        index_dict = defaultdict(deque)

        for i, n in enumerate(s):
            index_dict[n].append(i)
        
        out = [0]
        _max = 0
        last = -1
        for i, n in enumerate(s):
            if index_dict[n][-1] > _max:
                _max = index_dict[n][-1]

            if _max == i:
                out.append(i-last)
                _max = 0
                last = i
        
        return out[1:]