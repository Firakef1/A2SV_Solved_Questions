class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = Counter(nums)
        arr = []
        for key in frequency:
            arr.append([key, frequency[key]])

        arr.sort(key= lambda x: -x[1])

        out = [0]*k
        for i in range(k):
            out[i] = arr[i][0]

        return out