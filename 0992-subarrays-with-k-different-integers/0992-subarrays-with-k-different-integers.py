class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        ans = 0
        freq = defaultdict(int)

        for r in range(len(nums)):
            freq[nums[r]]+=1

            while len(freq)>k:
                freq[nums[left]]-=1

                if freq[nums[left]]==0:
                    del freq[nums[left]]

                left+=1
                right = left

            while left<len(nums) and freq[nums[left]]>1:
                freq[nums[left]]-=1
                left+=1

            if len(freq)==k:
                ans+=left-right+1

        return ans
            