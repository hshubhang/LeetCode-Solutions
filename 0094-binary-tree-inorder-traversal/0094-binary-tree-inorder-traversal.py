# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val = []
        def inorder(node):
            if not node:
                return []

            inorder(node.left)
            val.append(node.val)
            inorder(node.right)

            return val
        return inorder(root)