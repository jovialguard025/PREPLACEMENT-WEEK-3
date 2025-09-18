class Solution:
    def removeLoop(self, head):
        if head is None or head.next is None:
            return  

        slow = head
        fast = head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  
                break
        else:
            return 

       
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        
        ptr = slow
        while ptr.next != slow:  
            ptr = ptr.next
        ptr.next = None
