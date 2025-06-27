# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        sorted_arr = []
        def dfs(node):

            nonlocal sorted_arr

            if not node:
                return


            dfs(node.left)
            sorted_arr.append(node.val)
            dfs(node.right)

        dfs(root)
        left = 0
        right = len(sorted_arr)
        while left < right:
            mid = left + (right - left) // 2

            if sorted_arr[mid] > target:
                right = mid
            else:
                left = mid + 1

        if left == 0:
            return sorted_arr[0]  # All values are bigger than target
        elif left == len(sorted_arr):
            return sorted_arr[-1]  # All values are smaller than target
        else:
            # Compare the two closest neighbors
            before = sorted_arr[left - 1]
            after = sorted_arr[left]
            return before if abs(before - target) <= abs(after - target) else after
        
            