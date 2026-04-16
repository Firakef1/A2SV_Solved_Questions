# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node):
            if not node:
                return 0
            
            nonlocal res

            left = dfs(node.left)
            right = dfs(node.right)

            extra_coin = node.val + left + right - 1
            res += abs(extra_coin)

            return extra_coin
        
        dfs(root)

        return res
            
            
        