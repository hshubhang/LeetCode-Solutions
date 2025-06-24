# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def helper(node, low, high):
            nonlocal total
            if not node:
                return
            helper(node.left, low, high)
            helper(node.right, low, high)

            if low <= node.val <= high:
                total += node.val

        helper(root, low, high)
        return total

