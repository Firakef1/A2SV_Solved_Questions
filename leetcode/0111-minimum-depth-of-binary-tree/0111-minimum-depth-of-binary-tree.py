# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        

        queue = deque([root])
        depth = 0
        if not root:
            return 0
        
        while queue:
            
            depth += 1
            
            for _ in range(len(queue)):

                node = queue.popleft()
                if not node:
                    continue
            
                if not node.left and not node.right:
                    # print(queue)
                    return depth
                
                queue.append(node.left)
                queue.append(node.right)
            
            
       
            

