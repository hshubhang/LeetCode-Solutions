# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], first: int, last: int) -> Optional[ListNode]:
        if not head:
            return None
        left, right = head, head
        stop = False
        def recurseToReverse(right, first, last):
            nonlocal left, stop
            if last == 1:
                return
            right = right.next

            if first > 1:
                left = left.next
            recurseToReverse(right, first - 1, last - 1)

            if left == right or right.next == left:
                stop = True
            
            if not stop:
                left.val, right.val = right.val, left.val

                left = left.next

        recurseToReverse(right, first, last)

        return head


