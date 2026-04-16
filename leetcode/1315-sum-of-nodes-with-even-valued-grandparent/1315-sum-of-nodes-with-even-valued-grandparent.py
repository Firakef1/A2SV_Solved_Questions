# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node, even=False, expect=False):
            if not node:
                return
            
            nonlocal res

            if expect:
                res += node.val
            
            next_expect = True if even else False
            next_even = True if node.val%2 == 0 else False

            dfs(node.left, next_even, next_expect)
            dfs(node.right, next_even, next_expect)
        
        dfs(root)

        return res

        
    
        