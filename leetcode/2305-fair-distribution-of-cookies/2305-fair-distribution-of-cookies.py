class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True) 
        final = float("inf")
        arr = [0] * k
        
        def find(index):
            nonlocal final
            if index == len(cookies):
                final = min(final, max(arr))
                return
            
  
            if max(arr) >= final: 
                return

            for i in range(k):
      
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                
                arr[i] += cookies[index]
                find(index + 1)
                arr[i] -= cookies[index]
        
        find(0)
        return final
