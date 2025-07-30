# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node1, node2, carry):
            if not node1 and not node2 and carry == 0:
                return

            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            node = ListNode(digit)

            next1 = node1.next if node1 else None
            next2 = node2.next if node2 else None
            node.next = helper(next1, next2, carry)

            return node
        
        return helper(l1, l2, 0)

        