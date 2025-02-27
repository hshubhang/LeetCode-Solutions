# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result_arr = []

        def helper(node):
            if not node:
                return -1

            left_height = helper(node.left)
            right_height = helper(node.right)
            height = max(left_height, right_height) + 1

            if height == len(result_arr):
                result_arr.append([])
            result_arr[height].append(node.val)
            
            return height
        
        helper(root)
        return result_arr