
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reserve_k_groups(self, head, k) -> ListNode:
        if head is None or head.next is None:
            return head

        tmp = head_new = ListNode(0)
        head_new.next = head
        prev = head_new
        ptr = head

        while True:

            j = 1
            i = 1
            fast_ptr = ptr

            while j <= k:
                if fast_ptr is not None:
                    fast_ptr= fast_ptr.next
                    j += 1
                else:
                    return head_new.next
            
            pre_head = ptr

            while i <= k:
                next_ptr = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = next_ptr
                i += 1

            pre_head.next = ptr
            tmp.next = prev
            tmp = pre_head

        return head_new.next


def transfer_items_to_list(items) -> ListNode:
    dummy_ptr = ListNode(0)
    ptr = dummy_ptr

    for item in items:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return dummy_ptr.next

def transfer_list_to_string(head):
    if head is None:
        return '[]'

    string = ''
    while head:
        string += head.val + ', '
        head = head.next

    return '[' + string[:-2] + ']'

def main():
    items = input('please input : ')

    head = transfer_items_to_list(items)

    li = Solution().reserve_k_groups(head, 3)

    ret = transfer_list_to_string(li)
    print(ret)

if __name__ == '__main__':
    main()