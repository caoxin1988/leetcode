/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode head_new = new ListNode(0);
        head_new.next = head;
        ListNode pre_head = head;
        ListNode pre_tail = head_new;
        
        ListNode ptr = head;
        ListNode prev = head_new;
        
        ListNode fast = null;
        
        while (true) {
            fast = ptr;
            for (int i = 1; i <= k; i++) {
                if (fast != null)
                    fast = fast.next;
                else
                    return head_new.next;
            }
            
            pre_head = ptr;
            for (int i = 1; i <= k; i++) {
                ListNode next = ptr.next;
                ptr.next = prev;
                prev = ptr;
                ptr = next;
            }
            pre_head.next = ptr;
            pre_tail.next = prev;
            pre_tail = pre_head;
            
        }
    }
}