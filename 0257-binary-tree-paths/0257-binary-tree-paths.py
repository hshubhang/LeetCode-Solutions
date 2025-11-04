# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans_arr = []

        queue = deque([(root, str(root.val))])

        while queue:
            node, path = queue.popleft()

            if not node.left and not node.right:
                ans_arr.append(path)

            if node.left:
                queue.append((node.left, f"{path}" + "->" f"{node.left.val}"))
            if node.right:
                queue.append((node.right, f"{path}" + "->" + f"{node.right.val}"))

        
        return ans_arr