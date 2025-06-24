# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])

        ans = []
        depth = 0

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

            if depth % 2 == 0:
                ans.append(nodes_at_level)
            else:
                nodes_at_level.reverse()
                ans.append(nodes_at_level)
            depth += 1

        return ans
