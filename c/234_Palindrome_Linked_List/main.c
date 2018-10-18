bool isPalindrome(struct ListNode* head) {
    if ((head == NULL) || (head->next == NULL))
        return true;
    
    struct ListNode *fast_ptr = head;
    struct ListNode *slow_ptr = head;
    struct ListNode *prev = NULL;
    struct ListNode *next = NULL;
    
    while (fast_ptr && fast_ptr->next) {
        fast_ptr = fast_ptr->next->next;
        
        next = slow_ptr->next;
        slow_ptr->next = prev;
        prev = slow_ptr;
        slow_ptr = next;
    }
    
    if (fast_ptr && (fast_ptr->next == NULL)) {
        slow_ptr = slow_ptr->next;
    }
    
    while (slow_ptr) {
        if (slow_ptr->val != prev->val)
            return false;
        
        slow_ptr = slow_ptr->next;
        prev = prev->next;
    }
    
    return true;
}