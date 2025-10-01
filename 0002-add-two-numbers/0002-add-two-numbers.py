# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = sum_list = ListNode(float('inf'))
        carry = 0
        while l1 or l2 or carry:
            summ = carry
            if l1:
                summ += l1.val
            if l2:
                summ += l2.val

            carry = summ // 10
            node_val = summ % 10
            
            current.next = ListNode(node_val)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        
        return sum_list.next