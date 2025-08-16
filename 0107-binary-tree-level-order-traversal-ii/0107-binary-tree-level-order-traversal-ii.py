# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = deque()

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

            res.appendleft(nodes_at_level)

        return list(res)