class Solution:
    def removeLoop(self, head):

        
        if head is None or head.next is None:
            return False

       
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                break
        else:
            
            return False
        slow_ptr = head
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        ptr = slow_ptr
        while ptr.next != slow_ptr:
            ptr = ptr.next

        
        ptr.next = None
        return True
