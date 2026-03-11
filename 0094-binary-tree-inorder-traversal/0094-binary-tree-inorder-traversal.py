# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

   
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        def dfs(node, visted=set()):
            
            if not node:
                return 
            
            nonlocal arr
            
            left = node.left
            right = node.right
            visted.add(node)

            if left:
                if left not in visted:
                    dfs(left, visted)

            arr.append(node.val)

            if right:
                if right not in visted:
                    dfs(right, visted)
                        
            
        
        dfs(root)

        return arr 
        
     
        
