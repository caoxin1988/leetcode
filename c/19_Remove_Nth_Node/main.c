struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if ((head == NULL) && (head->next == NULL))
        return NULL;
    
    struct ListNode* fast_ptr = head;
    struct ListNode* slow_ptr = head;
    
    while (n-- > 0) {
        fast_ptr = fast_ptr->next;
    }
    
    if (fast_ptr == NULL)
        return head->next;
    
    while (fast_ptr->next) {
        fast_ptr = fast_ptr->next;
        slow_ptr = slow_ptr->next;
    }
    
    slow_ptr->next = slow_ptr->next->next;
    
    return head;
}