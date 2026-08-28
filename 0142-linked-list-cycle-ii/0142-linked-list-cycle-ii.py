# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Step 1: Determine if a cycle exists using fast and slow pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Cycle detected
            if slow == fast:
                # Step 2: Find the entry node of the cycle
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
                
        return None
        