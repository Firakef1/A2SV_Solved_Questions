class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def find(lis):
            if len(lis) <= 1:
                return [lis]
            
            result = []
            for i in range(len(lis)):
                cur = lis[i]
                
                others = lis[:i] + lis[i+1:]
                
                for p in find(others):
                    result.append([cur] + p)
                    
            return result
        
        return find(nums)