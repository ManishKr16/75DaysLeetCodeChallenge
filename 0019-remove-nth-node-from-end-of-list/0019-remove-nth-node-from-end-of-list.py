# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Handle the edge case: removing the head node
        if length == n:
            return head.next
            
        # Second pass: move to the node right before the target
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next
            
        # Skip the target node
        curr.next = curr.next.next
        return head