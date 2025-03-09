# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if (slow == fast):
                slow = head
                while slow != fast:
                    fast, slow = fast.next, slow.next
                return slow
        return None