/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode prev = dummy;
        prev.next = head;
            
        while ((prev.next != null) && (prev.next.next != null)) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;
                
            prev.next = second;
            first.next = second.next;
            second.next = first;
            prev = first;
        }
        
        return dummy.next;
    }
}