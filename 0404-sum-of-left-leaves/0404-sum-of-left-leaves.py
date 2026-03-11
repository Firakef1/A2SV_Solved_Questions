# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        total = 0

        def dfs(node, isNotRight=True):

            if not node:
                return

            nonlocal total

            if not isNotRight and not (node.left or node.right):
                total += node.val
            
            dfs(node.left, isNotRight=False)
            dfs(node.right)
        
        dfs(root)

        return total
        