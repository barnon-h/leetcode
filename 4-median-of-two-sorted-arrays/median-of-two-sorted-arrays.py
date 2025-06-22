from collections import deque

class Solution:
    def findMedianSortedArrays( self, 
                                nums1: List[ int ], 
                                nums2: List[ int ]
                            ) -> float:
        total_len = len( nums1 ) + len( nums2 )

        final_arr = deque([])
        n1 = deque( nums1 )
        n2 = deque( nums2 )

        for i in range( total_len ):
            p1 = n1.popleft() if len( n1 ) > 0 else None
            p2 = n2.popleft() if len( n2 ) > 0 else None

            if p1 is None:
                if p2 is None:
                    break
                elif p2 is not None:
                    final_arr.append( p2 )
                    if len( n2 ) > 0 : 
                        for j in n2 : final_arr.append( j )
                    break
            elif p2 is None:
                if p1 is None:
                    break
                elif p1 is not None:
                    final_arr.append( p1 )
                    if len( n1 ) > 0 : 
                        for j in n1 : final_arr.append( j )
                    break
            else:
                if p1 < p2:
                    final_arr.append( p1 )
                    n2.appendleft( p2 )
                elif p2 < p1:
                    final_arr.append( p2 )
                    n1.appendleft( p1 )
                elif p1 == p2:
                    final_arr.append(p1)
                    final_arr.append(p2)


        median = -1
        if len(final_arr) == 1:
            median = final_arr[0]
        elif total_len%2 == 1:
            median = final_arr[ floor(total_len/2) ]
        else:
            mid = floor(total_len/2)
            median = (final_arr[mid] + final_arr[mid-1]) / 2
        return median


        