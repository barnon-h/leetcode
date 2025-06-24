# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sum_link(self, l: Optional[ListNode]):
        curr = l
        val = 0
        multiplier = 1
        while 1:
            val += curr.val * multiplier
            curr = curr.next
            multiplier = multiplier * 10
            if curr is None: break
        return val

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        char_array = [*f"{ self.sum_link(l1) + self.sum_link(l2) }"]
        char_array.reverse()
        
        l = ListNode( int( char_array[ 0 ]), None )
        
        curr = l
        for i in range(1, len(char_array)):
            curr.next = ListNode(int(char_array[i]), None)
            curr = curr.next
    
        return l

        