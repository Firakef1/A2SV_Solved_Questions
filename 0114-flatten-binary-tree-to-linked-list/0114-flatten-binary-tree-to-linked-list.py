# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        out = []

        def preorder(node):

            if not node:
                return 
            
            nonlocal out
            out.append(node)

            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        
        if not out:
            return 

        for i in range(len(out)-1):
            out[i].left = None
            out[i].right = out[i+1]

        out[-1].left = None
        out[-1].right = None