class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        general_sum = sum([x for x in nums if x%2 == 0])
        return_arr = []

        for queri in queries:
            add_num = queri[0]
            index = queri[1]
            num = nums[index]

            if num%2 == 0:
                if (num+add_num)%2 == 1:
                    general_sum -= num
                else:
                    general_sum += add_num
            
            else:
                if (num+add_num)%2 == 0:
                    general_sum += num+add_num
            
            return_arr.append(general_sum)
            nums[index] += add_num

        return return_arr