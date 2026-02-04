#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        
        freq_a = Counter(a)
        freq_b = Counter(b)

        for key in freq_b:
            if freq_a[key] < freq_b[key]:
                return False
        return True
                
    
    
    
    
