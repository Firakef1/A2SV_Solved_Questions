class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def inversion_sort(lis):

            if len(lis) <= 1:
                return lis

            mid = len(lis)//2

            one = inversion_sort(lis[:mid])
            two = inversion_sort(lis[mid:])

            return merge(one, two)

        def merge(left_half, right_half):
            if not right_half or not left_half:
                return right_half or left_half
            left = 0
            right = 0
            out = []
            prefix = [0]*len(left_half)

            while left < len(left_half) and right < len(right_half):
                if left_half[left][0] <= right_half[right][0]:
                    # right_half[right][1] += 1
                    out.append(left_half[left])
                    left += 1
                else:
                    prefix[left] += 1
                    out.append(right_half[right])
                    right += 1
            
            #calculate prefix sum
            prefix = [0]+prefix
            for i in range(1, len(prefix)):
                prefix[i] = prefix[i-1]+prefix[i]
            prefix = prefix[1:]

            #add the number of smaller elements
            for i in range(len(prefix)):
                left_half[i][1] += prefix[i]
            
            out.extend(left_half[left:])
            out.extend(right_half[right:])
            return out
        
        nums = [[x, 0, i] for i, x in enumerate(nums)]

        nums = inversion_sort(nums)
        # print(nums)
        out = [0]*len(nums)

        for i in nums:
            out[i[2]] = i[1]

        return out

        