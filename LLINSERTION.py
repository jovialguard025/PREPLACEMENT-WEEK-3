class Solution:
    def insertAtEnd(self, head, value_to_insert):
        new_node = Node(value_to_insert)
        
        if head is None:
            return new_node
        
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
        
        return head