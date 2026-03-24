# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        arr = []

        def inorder(node):
            if not node:
                return
            
            nonlocal arr

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        # print(arr)
        left, right = 0, len(arr)-1

        while left < right:
            val = arr[left] + arr[right]
            if val == k:
                return True
            
            elif val < k:
                left += 1
            
            else:
                right -= 1
        
        return False


