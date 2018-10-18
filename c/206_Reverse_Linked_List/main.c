struct ListNode* reverseList(struct ListNode* head) {
    if ((head == NULL) || (head->next == NULL))
        return head;
    
    struct ListNode *prev = NULL;
    struct ListNode *next = NULL;
    struct ListNode *ptr = head;
    
    while (ptr) {
        next = ptr->next;
        ptr->next = prev;
        prev = ptr;
        ptr = next;
    }
    
    return prev;
}