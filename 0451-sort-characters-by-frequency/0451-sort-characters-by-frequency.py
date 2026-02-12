class Solution:
    def frequencySort(self, s: str) -> str:

        
        count = Counter(s)

        lis = list(map(str, s))

        lis.sort(key=lambda x: (count[x], x), reverse=True)

        return "".join(lis)
        