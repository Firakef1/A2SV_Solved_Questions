# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def find(node, state):
            nonlocal out

            if not node:
                out.append(None)
                return
            
            find(node.left if state else node.right, state)
            find(node.right if state else node.left, state)

            out.append(node.val)
        
        out = []
        find(root, True)
        normal = out[::]
        out = []
        find(root, False)
        print(out, normal)
        return out == normal