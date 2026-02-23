class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      
        freq = Counter(nums)
        new = []
        for i in freq:
            if len(new) == 2:
                break
    
            if freq[i] > len(nums)/3:
                new.append(i)

        return new