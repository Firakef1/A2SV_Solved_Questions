# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur = 0
        _max = 0

        def dfs(node):
            nonlocal cur, _max
            if not node:
                return
            
            left = node.left
            right = node.right
            cur += 1
            dfs(left)
            dfs(right)
            _max = max(cur, _max)
            
            cur -= 1
           
        
        dfs(root)

        return _max