class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = defaultdict(int)

        for i in responses:
            for j in list(set(i)):
                freq[j] += 1
        
        common = responses[0][0]
        for i in freq:
            if freq[common] < freq[i]:
                common = i
            elif freq[common] == freq[i]:
                common = min(common, i)

        return common