# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans_arr = []
        ans = float('inf')
        def helper(node):

            if not node:
                return
            nonlocal ans_arr

            helper(node.left)
            ans_arr.append(node.val)
            helper(node.right)

        helper(root)
        for i in range(1, len(ans_arr)):
            ans = min(ans, abs(ans_arr[i] - ans_arr[i-1]))

        return ans

        