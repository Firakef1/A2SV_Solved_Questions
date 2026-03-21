# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = 0

        def dfs(node, arr=[0]):

            if not node:
                return

            nonlocal targetSum, count
            

            for i, n in enumerate(arr):
                arr[i] = n+node.val

                if arr[i] == targetSum:
                    count += 1
                    # print(arr)
            
            # print(arr, "left")
            dfs(node.left, arr+[0])
            # print(arr, "right")
            dfs(node.right, arr+[0])
        
        dfs(root)

        return count