class Solution:
    def getKthFromLast(self, head, k):
        
        slow = head
        fast = head

        
        for _ in range(k):
            if fast is None:  
                return -1
            fast = fast.next

        
        while fast is not None:
            slow = slow.next
            fast = fast.next

        #slow now points to the kth node from the end
        return slow.data if slow is not None else -1