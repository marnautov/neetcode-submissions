# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            total = node.val if low <= node.val <= high else 0

            if node.val > low:
                total += dfs(node.left)

            if node.val < high:
                total += dfs(node.right)

            return total

        return dfs(root)
        