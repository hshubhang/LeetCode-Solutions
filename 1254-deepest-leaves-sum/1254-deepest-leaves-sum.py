# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        queue = deque([root])
        while queue:
            curr_level = len(queue)
            ans = 0
            for i in range(curr_level):

                node = queue.popleft()

                if not node.left and not node.right:
                    ans += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
