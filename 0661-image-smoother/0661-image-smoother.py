class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        smoothed_matrix = []

        for i in range(len(img)):
            smoothed_row =[]
            for j in range(len(img[0])):
                total = img[i][j]
                counter = 1

                if i-1 >= 0:
                    total += img[i-1][j]
                    counter += 1

                if i+1 < len(img):
                    total += img[i+1][j]
                    counter += 1
                
                if j-1 >= 0:
                    total += img[i][j-1]
                    counter += 1
                
                if j+1 < len(img[0]):
                    total += img[i][j+1]
                    counter += 1
                
                if i-1 >= 0 and j-1 >= 0:
                    total += img[i-1][j-1]
                    counter += 1
                
                if i-1 >= 0 and j+1 < len(img[0]):
                    total += img[i-1][j+1]
                    counter += 1
                
                if  i+1 < len(img) and j-1 >= 0:
                    total += img[i+1][j-1]
                    counter += 1
                
                if i+1 < len(img) and j+1 < len(img[0]):
                    total += img[i+1][j+1]
                    counter += 1
                
                total = total//counter
                smoothed_row.append(total)
            
            smoothed_matrix.append(smoothed_row)
        
        return smoothed_matrix