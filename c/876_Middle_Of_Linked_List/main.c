/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    if ((head == NULL) && (head->next == NULL))
        return head;
    
    struct ListNode *fast_ptr = head;
    struct ListNode *slow_ptr = head;
    
    while (fast_ptr && fast_ptr->next) {
        fast_ptr = fast_ptr->next->next;
        slow_ptr = slow_ptr->next;
    }
    
    return slow_ptr;
}