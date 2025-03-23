# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def preorderHelper(node):
            if not node:
                return 0
            total = 0
            if low <= node.val <= high:
                total += node.val
            total += preorderHelper(node.left)
            total += preorderHelper(node.right)
            return total
        return preorderHelper(root)