# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
            
        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
                
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def isSameTree(node, subNode):
            if not node and not subNode:
                return True
            if not node and subNode or node and not subNode:
                return False
            if node.val != subNode.val:
                return False
            leftSide = isSameTree(node.left, subNode.left)
            rightside = isSameTree(node.right, subNode.right)
            
            return leftSide and rightside
        
        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
       

    
