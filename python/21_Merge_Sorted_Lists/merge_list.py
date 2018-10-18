class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge_list(self, l1, l2):
        
        dummy = ListNode(0)
        ptr = dummy

        while l1 or l2:
            # print('l1.value : %s, l1.value : %s' % (l1.val, l2.val))
            if l1 is None:
                ptr.next = l2
                return dummy.next
            
            if l2 is None:
                ptr.next = l1
                return dummy.next

            if l1.val >= l2.val:
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
                ptr.next = None
            else:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
                ptr.next = None

        return dummy.next
                

def transfer_list_to_string(head):
    if head is None:
        return '[]'

    string = ''
    while head:
        string += str(head.val) + ', '
        head = head.next

    return '[' + string[:-2] + ']'


def transfer_string_to_list(items):
    dummy_ptr = ListNode(0)
    ptr = dummy_ptr

    for item in items:
        ptr.next = ListNode(item)
        ptr = ptr.next

    ptr = dummy_ptr.next

    return ptr


def main():
    items1 = input('please input string1 : ')
    items2 = input('please input string2 : ')

    head1 = transfer_string_to_list(items1)
    head2 = transfer_string_to_list(items2)

    s = Solution().merge_list(head1, head2)

    ret = transfer_list_to_string(s)

    print(ret)

if __name__ == '__main__':
    main()