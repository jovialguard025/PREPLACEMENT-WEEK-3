int getKthFromLast(struct Node* head, int k) {
    
    struct Node* slow = head;
    struct Node* fast = head;

   
    for (int i = 0; i < k; i++) {
        if (fast == NULL) {
            return -1;  
        }
        fast = fast->next;
    }

    
    while (fast != NULL) {
        slow = slow->next;
        fast = fast->next;
    }

  
    if (slow != NULL) {
        return slow->data;
    }
    return -1;  // Fallback (shouldn’t normally happen)
}