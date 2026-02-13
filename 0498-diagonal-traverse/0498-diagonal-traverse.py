class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        group = defaultdict(list)
        output = [0]*(len(mat)*len(mat[0]))

        #group the elemnts with the same index sum together
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                group[i+j].append([i, j])
        
        # print(group)


        ptr = 0
        order = False
        for key in group:
            arr = group[key]
            #the order is zig sag so we need to filip the arrays every iteration
            if order:
                arr.reverse()
            
            #if the lenght of the array is one it the direction of traversal does not matter so we don't need to filip the order
            if len(arr) > 1:
                order = not order
            
            #inserting the elemnts into the new array and then moving the pointer for the new array
            for i, j in arr:
                output[ptr] = mat[i][j]
                ptr += 1

        return output
