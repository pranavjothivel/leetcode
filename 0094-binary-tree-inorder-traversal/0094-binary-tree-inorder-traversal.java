/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> lst = new LinkedList<>();
        inorder(root, lst);
        return lst;
    }

    private void inorder(TreeNode node, List<Integer> lst) {
        if (node == null) {
            return;
        }

        inorder(node.left, lst);
        lst.add(node.val);
        inorder(node.right, lst);
    }
}