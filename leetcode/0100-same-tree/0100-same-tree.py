# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        state = True

        def dfs(node_one, node_two):
            nonlocal state

            if not node_one or not node_two:
                if not (not node_one and not node_two):
                    state = False
                
                return
            
            if node_one.val != node_two.val:
                state = False
            
            if not state:
                return
            
            left_one = node_one.left
            left_two = node_two.left

            right_one = node_one.right
            right_two = node_two.right

            if left_one and left_two:
                dfs(left_one, left_two)
            elif left_one or left_two:
                state = False
            
            if not state:
                return
            
            if right_one and right_two:
                dfs(right_one, right_two)
            elif right_one or right_two:
                state = False
        
        dfs(p, q)

        return state