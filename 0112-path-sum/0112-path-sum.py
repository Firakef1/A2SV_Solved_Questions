# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        state = False
        total = 0
        def dfs(node):
            nonlocal state, total

            if not node or state:
                return

            total += node.val

            if total == targetSum and not (node.left or node.right):
                state = True
            
            left = node.left
            right = node.right

            dfs(left)
            dfs(right)

            total -= node.val
        
        dfs(root)
        return state