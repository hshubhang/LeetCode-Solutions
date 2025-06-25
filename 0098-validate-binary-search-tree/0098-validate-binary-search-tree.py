# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, small, large):

            if not node:
                return True

            if not (small < node.val < large):
                return False

            left = helper(node.left, small, node.val)
            right = helper(node.right, node.val, large)

            return left and right

        return helper(root, float("-inf"), float("inf"))
