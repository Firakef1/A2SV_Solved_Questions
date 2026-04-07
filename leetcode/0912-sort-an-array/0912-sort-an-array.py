class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_half,right_half) -> List[int]:
            # write your code here
            one = 0
            two = 0
            ptr = 0
            
            res = [0]*(len(left_half)+len(right_half))
            
            while one < len(left_half) and two < len(right_half):
                if left_half[one] < right_half[two]:
                    res[ptr] = left_half[one]
                    one += 1
                    
                else:
                    res[ptr] = right_half[two]
                    two += 1
                ptr += 1
            
            while one < len(left_half):
                res[ptr] = left_half[one]
                one += 1
                ptr += 1
            
            while two < len(right_half):
                res[ptr] = right_half[two]
                two += 1
                ptr += 1
            return res
        
        def mergeSort(lis):
            n = len(lis)
            if n < 2:
                return lis
            
            middle = n//2

            left_half = mergeSort(lis[:middle])
            right_half = mergeSort(lis[middle:])

            return merge(left_half, right_half)
        
        return mergeSort(nums)