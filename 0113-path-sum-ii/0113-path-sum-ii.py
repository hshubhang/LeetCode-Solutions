# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def helper(node, targetSum, path):
            if not node:
                return

            targetSum -= node.val
            new_path = path + [node.val]

            if not node.left and not node.right and targetSum == 0:
                ans.append(new_path)

            helper(node.left, targetSum, new_path)
            helper(node.right, targetSum, new_path)

        helper(root, targetSum, [])
        return ans


