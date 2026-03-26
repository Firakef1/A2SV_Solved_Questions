# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode()
        root.val = preorder[0]

        if len(preorder)==1:
            return root
        

        left_child = preorder[1]
        right_child= postorder[-2]


        if left_child == right_child:
            root.left = self.constructFromPrePost(preorder[1:], postorder[:-1])
        else:
            right_index = preorder.index(right_child)
            left_index = postorder.index(left_child)

            root.left = self.constructFromPrePost(preorder[1:right_index], postorder[:left_index+1])
            root.right = self.constructFromPrePost(preorder[right_index:], postorder[left_index+1:-1])
        
        return root