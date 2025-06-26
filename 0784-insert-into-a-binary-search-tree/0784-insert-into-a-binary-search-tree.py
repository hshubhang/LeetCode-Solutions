# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val and not root.left:
            root.left = TreeNode(val)
        elif val > root.val and not root.right:
            root.right = TreeNode(val)
        
        if val < root.val:
            self.insertIntoBST(root.left, val)
        elif val > root.val:
            self.insertIntoBST(root.right, val)

        return root
        

