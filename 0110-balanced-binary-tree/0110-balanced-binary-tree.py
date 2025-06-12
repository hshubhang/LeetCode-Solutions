# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return  0 , True

            left_side, left_balanced = helper(node.left)
            right_side, right_balanced = helper(node.right)

            current_height = 1 + max(left_side, right_side)

            is_balanced = left_balanced and right_balanced and abs(left_side - right_side) <=1

            return current_height, is_balanced

        _, balanced = helper(root)

        return balanced