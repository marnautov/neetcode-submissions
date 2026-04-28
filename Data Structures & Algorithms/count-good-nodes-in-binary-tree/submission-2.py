# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        

        def dfs(node, max_value) -> int:
            if not node:
                return 0

            good = 1 if node.val >= max_value else 0

            max_value = max(max_value, node.val)

            return good + dfs(node.left, max_value) + dfs(node.right, max_value)

        return dfs(root, root.val)
        