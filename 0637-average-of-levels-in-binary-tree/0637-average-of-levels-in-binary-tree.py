# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []

        queue = deque([root])

        while queue:

            curr_level = len(queue)
            nodes_at_level = []


            for i in range(curr_level):

                node = queue.popleft()
                nodes_at_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = sum(nodes_at_level) / curr_level

            res.append(average)

        return res