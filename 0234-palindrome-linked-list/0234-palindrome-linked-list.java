/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.Stack;
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode iterator = head;
        Stack listStack = new Stack();
        while (iterator != null) {
            listStack.push(iterator.val);
            iterator = iterator.next;
        }
        iterator = head;
        while (!listStack.isEmpty()) {
            if (iterator.val != (int) listStack.pop()) {
                return false;
            }
            iterator = iterator.next;
        }
        return true;
    }
}