class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        lis = list(zip(heights, names))

        lis.sort(key=lambda x: -x[0])

        for i in range(len(lis)):
            names[i] = lis[i][1]

        return names