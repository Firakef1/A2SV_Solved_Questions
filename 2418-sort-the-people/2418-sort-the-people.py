class Solution:
    def radix_sort(self, arr):
        if not arr:
            return arr

        output = arr.copy()
        max_num = max(output)
        exp = 1 

        while max_num // exp > 0:
            n = len(output)
            count = [0] * 10
            temp = [0] * n

 
            for num in output:
                digit = (num // exp) % 10
                count[digit] += 1

     
            for i in range(1, 10):
                count[i] += count[i - 1]

  
            for i in range(n - 1, -1, -1):
                digit = (output[i] // exp) % 10
                temp[count[digit] - 1] = output[i]
                count[digit] -= 1

            output = temp
            exp *= 10

        return output

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        lis = dict(zip( heights, names))

        heights = self.radix_sort(heights)

        for i in range(len(heights)):
            names[i] = lis[heights[i]]

        return names[::-1]
        