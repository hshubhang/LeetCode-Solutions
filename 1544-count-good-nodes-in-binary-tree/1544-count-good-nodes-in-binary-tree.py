# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        count = 0
        def goodNodeCounter(node, maxSoFar):
            
            if not node:
                return 0
            nonlocal count
            if node.val >= maxSoFar:
                maxSoFar = node.val
                count += 1


            goodNodeCounter(node.left, maxSoFar)
            goodNodeCounter(node.right, maxSoFar)
        
        goodNodeCounter(root, root.val)
        return count