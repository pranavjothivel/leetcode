# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        num1 = ""
        num2 = ""

        curr = l1
        while curr:
            stack.append(curr.val)
            curr = curr.next
        

        while len(stack) != 0:
            num1 += str(stack.pop())
        num1 = int(num1)

        stack = []

        curr = l2
        while curr:
            stack.append(curr.val)
            curr = curr.next
        

        while len(stack) != 0:
            num2 += str(stack.pop())
        num2 = int(num2)

        stack = []

        sum = num1 + num2
        sum_list = list(str(sum))[::-1]
        
        sum_node = ListNode(int(sum_list[0]))
        prev = sum_node

        for i in range(1, len(sum_list)):
            new_node = ListNode(int(sum_list[i]))
            prev.next = new_node
            prev = new_node
        
        return sum_node