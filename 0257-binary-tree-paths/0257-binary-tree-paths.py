# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans_arr = []
        if not root:
            return []
        def helper(node, new_str):

            if not node:
                return
                
            if node:
                new_str += f"{node.val}"

            if not node.left and not node.right:
                ans_arr.append(new_str)

            else:

                new_str += "->"

                helper(node.left, new_str)
                helper(node.right, new_str)

        helper(root, "")

        return ans_arr
