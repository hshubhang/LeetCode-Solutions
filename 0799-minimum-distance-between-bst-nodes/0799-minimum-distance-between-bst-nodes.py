# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans_arr = []

        ans = float('inf')

        def dfs(node):

            if not node:
                return

            
            dfs(node.left)
            ans_arr.append(node.val)
            dfs(node.right)

        
        dfs(root)
        for i in range(1, len(ans_arr)):
            ans = min(ans, abs(ans_arr[i] - ans_arr[i-1]))

        return ans