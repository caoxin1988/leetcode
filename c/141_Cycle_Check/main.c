/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

bool hasCycle(struct ListNode *head) {
    
    if (head == NULL)
        return false;
    
    struct ListNode *fast_ptr = head->next;
    struct ListNode *slow_ptr = head;
    
    while (fast_ptr != slow_ptr) {
        if ((fast_ptr == NULL) || (fast_ptr->next == NULL))
            return false;
        
        fast_ptr = fast_ptr->next->next;
        slow_ptr = slow_ptr->next;
    }
    
    return true;
}