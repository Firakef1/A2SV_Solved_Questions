class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        
        def traverse(node):
            if not node:

                return True, 0, float('inf'), float('-inf')
            
            left_BST, left_sum, left_min, left_max = traverse(node.left)
            right_BST, right_sum, right_min, right_max = traverse(node.right)

            if (left_BST and right_BST and left_max < node.val < right_min):
                
                current_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, current_sum)
                

                return True, current_sum, min(node.val, left_min), max(node.val, right_max)
            
            return False, 0, 0, 0
            
        traverse(root)
        return self.max_sum