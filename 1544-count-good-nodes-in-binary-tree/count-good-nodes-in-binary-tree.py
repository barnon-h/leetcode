# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_good_node( self,
                      prnt_val : int, 
                      n : TreeNode
                      ) -> bool:
        return n.val >= prnt_val

    def is_leaf( self, n : TreeNode ) -> bool:
        return n.right is None and n.left is None

    def get_score( self, prnt_val : int, n : TreeNode ) -> int:
        print(f"# Evaluating node {n.val}, with max node {prnt_val}")
        return 1 if self.is_good_node( prnt_val, n ) else 0

    def count_good_nodes( self, prnt_val : int, n : TreeNode ) -> int:
        if self.is_leaf( n ):
            x = self.get_score(prnt_val, n)
            print(f"adding {x}")
            return x
        
        else:
            score = self.get_score( prnt_val, n )
            print(f"adding {score}")
            max_val = max([ prnt_val, n.val ])
            
            if n.left and n.right:
                return score + self.count_good_nodes( max_val, n.left ) + self.count_good_nodes( max_val, n.right )
            
            elif n.left is None:
                return score + self.count_good_nodes(max_val, n.right)
            
            elif n.right is None:
                return score + self.count_good_nodes(max_val, n.left)


    def goodNodes( self, root: TreeNode ) -> int:
        return self.count_good_nodes( -math.inf, n = root )