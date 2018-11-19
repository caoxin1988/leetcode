class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sort_list(self, head : ListNode):

        if not head or not head.next:
            return head

        # break into two list
        prev = slow = fast = head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next

        prev.next = None

        # print('-------')
        # ptr = head
        # while ptr:
        #     print(ptr.val)
        #     ptr = ptr.next

        # print('=======')
        # ptr = slow
        # while ptr:
        #     print(ptr.val)
        #     ptr = ptr.next

        left = self.sort_list(head)
        right = self.sort_list(slow)

        ptr = dummy = ListNode(0)
        while left or right:
            
            if not left:
                ptr.next = right
                break

            if not right:
                ptr.next = left
                break

            if left.val > right.val:
                ptr.next = right
                right = right.next
            else:
                ptr.next = left
                left = left.next

            ptr = ptr.next

        return dummy.next
        

def transfor_list_to_string(head : ListNode):
    if not head:
        return ''

    string = ''
    while head:
        string += str(head.val) + ', '
        head = head.next

    return '[' + string[:-2] + ']'


def transfor_string_to_list(items: str):
    dummp_ptr = ListNode(0)
    ptr = dummp_ptr

    for item in items:
        ptr.next = ListNode(int(item))
        ptr = ptr.next

    return dummp_ptr.next

def main():
    items = input('please input : ')
    head = transfor_string_to_list(items)

    solution = Solution()
    # solution.sort_list(head)
    l = solution.sort_list(head)

    string = transfor_list_to_string(l)

    print(string)


if __name__ == '__main__':
    main()