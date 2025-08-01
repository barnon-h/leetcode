# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        elif root.val == val:
            return root
        else:
            if val > root.val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)

        