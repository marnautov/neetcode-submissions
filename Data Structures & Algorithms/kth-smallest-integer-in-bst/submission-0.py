# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        level = 0
        
        def dfs(node: Optional[TreeNode]) -> int | None:
            nonlocal level
            
            if not node:
                return
            
            left = dfs(node.left)
            if left is not None:
                return left

            level += 1
            if level == k:
                return node.val

            right = dfs(node.right)
            if right is not None:
                return right

            return None

        return dfs(root)
        