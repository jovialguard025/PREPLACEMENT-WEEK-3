class Solution:
    def detectLoop(self, head):
        
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

           
            if slow == fast:
                return True

        # No loop found
        return False