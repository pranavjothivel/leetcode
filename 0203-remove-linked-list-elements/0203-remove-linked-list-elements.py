# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.val != val:
                prev.next = current
                prev = prev.next
            current = current.next
        prev.next = None
        
        # current = dummy.next

        # while current and current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #     current = current.next
        
        return dummy.next