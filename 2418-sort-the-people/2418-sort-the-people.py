class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        lis = list(zip(heights, names))

        for i in range(len(lis)):
            for j in range(1, len(lis)-i):
                if lis[j][0] < lis[j-1][0]:
                    lis[j], lis[j-1] =  lis[j-1], lis[j]

        print(lis)
        
        for i in range(len(lis)):
            names[i] = lis[i][1]

        names = names[::-1]
        
        return names