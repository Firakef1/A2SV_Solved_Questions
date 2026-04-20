class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def find_pivot(lis, start, end):
            mid = (start + end) // 2
            a, b, c = lis[start], lis[mid], lis[end]
            
            if (b <= a <= c) or (c <= a <= b):
                return start
            if (a <= b <= c) or (c <= b <= a):
                return mid
            return end


        def partition(lis, start, end):
            pivot_index = find_pivot(lis, start, end)
            pivot_val = lis[pivot_index]
            
            lis[pivot_index], lis[start] = lis[start], lis[pivot_index]
            
            low = start + 1
            high = end

            while True:
                while low <= high and lis[low] <= pivot_val:
                    low += 1
                while low <= high and lis[high] >= pivot_val:
                    high -= 1
                
                if low <= high:
                    lis[low], lis[high] = lis[high], lis[low]
                else:
                    break

            lis[start], lis[high] = lis[high], lis[start]
            return high


        def quick_sort(lis, start, end):
            if start < end:
                p = partition(lis, start, end)
                quick_sort(lis, start, p - 1)
                quick_sort(lis, p + 1, end)
        

        quick_sort(nums, 0, len(nums)-1)
            