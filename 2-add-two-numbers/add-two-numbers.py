# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sum_link( self, 
                  l: Optional[ListNode]
                ) -> float:
        curr = l
        val = 0
        multiplier = 1
        while 1:
            val += curr.val * multiplier
            curr = curr.next
            multiplier = multiplier * 10
            if curr is None: break
        return val

    def addTwoNumbers( self, 
                        l1: Optional[ListNode], 
                        l2: Optional[ListNode]
                    ) -> Optional[ListNode]:
        char_array = [ *f"{ self.sum_link(l1) + self.sum_link(l2) }" ]
        
        l = ListNode( int( char_array[ len(char_array) -1 ]), None )
        
        curr = l
        for i in range( len( char_array ) -2, -1, -1):
            curr.next = ListNode( int( char_array[ i ]), None )
            curr = curr.next
    
        return l

        