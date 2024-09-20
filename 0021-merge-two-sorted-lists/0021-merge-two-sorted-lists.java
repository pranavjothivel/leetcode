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
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // recursive SLL
        // mergedList first node is empty value
        ListNode mergedList = new ListNode();
        ListNode cursor = mergedList;
        
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                cursor.next = list1;
                list1 = list1.next;
            }
            else {
                cursor.next = list2;
                list2 = list2.next;
            }
            cursor = cursor.next;

        }

        if (list1 != null) {
            cursor.next = list1;
        }
        else {
            cursor.next = list2;
        }

        return mergedList.next;
    }
}