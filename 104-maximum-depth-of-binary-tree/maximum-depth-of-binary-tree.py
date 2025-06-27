# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, n: Optional[ TreeNode ]) -> int:
        if n.left is None and n.right is None:
            return 1
        else:
            if n.left and n.right:
                l = 1 + self.dfs(n.left)
                r = 1 + self.dfs(n.right)
                return max([r,l])
            elif n.right is None:
                return 1 + self.dfs(n.left)
            elif n.left is None:
                return 1 + self.dfs(n.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            return self.dfs(root)
        else:
            return 0
        