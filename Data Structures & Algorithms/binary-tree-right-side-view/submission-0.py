# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque()
        q.append((1, root))

        res = {} # level : node

        while q:
            level, node = q.popleft()

            res[level] = node.val

            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
        
        return list(res.values())

            


        