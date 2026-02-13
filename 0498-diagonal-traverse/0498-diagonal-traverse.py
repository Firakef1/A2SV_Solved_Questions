class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        group = defaultdict(list)
        output = [0]*(len(mat)*len(mat[0]))

        for i in range(len(mat[0])):
            for j in range(len(mat)):
                group[i+j].append([i, j])
        
        print(group)
        ptr = 0
        order = True
        for key in group:
            arr = group[key]
            if order:
                arr.reverse()
            
            if len(arr) > 1:
                order = not order
            
            for i, j in arr:
                output[ptr] = mat[j][i]
                ptr += 1

        return output
