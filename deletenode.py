class Solution:
    def deleteNode(self, head, position):
        
        if head is None:
            return None

        
        if position == 1:
            return head.next

        
        current = head
        for _ in range(position - 2): 
            if current is None or current.next is None:
                return head  
            current = current.next

        #the target node (if exists)
        if current.next is not None:
            current.next = current.next.next

        return head