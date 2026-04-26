# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, node1):
            if not node and not node1:
                return True

            if not node or not node1:
                return False

            if node.val != node1.val:
                return False
      
            left = dfs(node.left, node1.left)
            if not left:
                return False

            right = dfs(node.right, node1.right)
            if not right:
                return False
            
            return True

        return dfs(p, q)


        