# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([[root, 0]])
        out = defaultdict(list)
        while queue:
            node, level = queue.popleft()
            if not node:
                continue

            queue.append([node.left, level+1])
            queue.append([node.right, level+1])

            out[level].append(node.val)

        value = []
        even = False 
        for i in out:
            value.append(out[i][::-1] if even else out[i])
            even = not even

        return value