# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        def preorderHelper(node):
            if not node:
                return
            nonlocal sum
            if low <= node.val <= high:
                sum += node.val
            preorderHelper(node.left)
            preorderHelper(node.right)
        preorderHelper(root)
        return sum