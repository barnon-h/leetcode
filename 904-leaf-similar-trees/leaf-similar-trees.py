# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_leaf( self, n:Optional[ TreeNode ]):
        return n.left is None and n.right is None

    def get_all_leaf( self, n:Optional[ TreeNode ]) -> list:
        if self.is_leaf( n ):
            return [ n.val ]
        
        else:
            if n.right is None:
                return self.get_all_leaf( n.left )
            
            elif n.left is None:
                return self. get_all_leaf( n.right )
            
            elif n.right and n.left:
                ret = []
                ret.extend(self.get_all_leaf( n.right ))
                ret.extend(self.get_all_leaf( n.left ))
                return ret
                

    def leafSimilar(self, 
                    root1: Optional[ TreeNode ], 
                    root2: Optional[ TreeNode ]
                    ) -> bool:

        n1 = self.get_all_leaf( root1 )
        n2 = self.get_all_leaf( root2 )
        
        ret = True
        if len( n1 ) != len( n2 ):ret = False
        else:
            for i in range( len( n1 )):
                if n1[ i ] != n2[ i ]: ret = False
        
        return ret
        