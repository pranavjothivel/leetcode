# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def inorder(node, lst):
        #     if node == None:
        #         return lst
        #     inorder(node.left, lst)
        #     lst.append(node.val)
        #     inorder(node.right, lst)
        #     return lst
        # return inorder(root, [])
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)

        # O(n) - space and time