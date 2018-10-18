/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode head;
    head.next = NULL;
    struct ListNode *ptr = &head;

    
    while (l1 || l2) {
        
        if (l1 == NULL) {
            ptr->next = l2;
            return head.next;
        } else if(l2 == NULL) {
            ptr->next = l1;
            return head.next;
        }
        
        if (l1->val >= l2->val) {
            ptr->next = l2;
            l2 = l2->next;
        } else {
            ptr->next = l1;
            l1 = l1->next;
        }
        
        ptr = ptr->next;
        ptr->next = NULL;
    }
    
    return head.next;
}