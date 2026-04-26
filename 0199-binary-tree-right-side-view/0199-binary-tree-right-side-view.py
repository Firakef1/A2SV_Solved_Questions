# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        value = [None]*101

        def dfs(node, depth=0):
            if not node:
                return
            
            nonlocal value
            value[depth]= node.val

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root)
        out = []

        for i in value:
            if i != None:
                out.append(i)
        
        return out