class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_minimum_node(self, lists:list) -> ListNode:
        minimum = lists[0]

        for item in lists:
            if item.val < minimum.val:
                minimum = item

        return minimum

    def mergeKList(self, lists : list) -> ListNode:
        k_value = []
        dummy_ptr = ptr = ListNode(0)

        for l in lists:
            if l:
                k_value.append(l)

        while k_value:
            '''get the minimum data from the list and append the next value into this list'''
            node = self.get_minimum_node(k_value)
            k_value.remove(node)

            ptr.next = ListNode(node.val)
            ptr = ptr.next

            if node.next:
                k_value.append(node.next)

        return dummy_ptr.next


def transfer_list_to_ListNode():
    list_input = [[1,4,5], [1,3,4], [2,6]]
    lists = []

    for sub_list in list_input:
        dummy_ptr = ListNode(0)
        ptr = dummy_ptr
        for item in sub_list:
            ptr.next = ListNode(item)
            ptr = ptr.next
        lists.append(dummy_ptr.next)

    return lists

def transfer_list_to_string(lists:list):
    for items in lists:
        string = ''
        head = items
        while head:
            string = string + str(head.val) + ', '
            head = head.next

        print('[' + string[:-2] + ']')

def print_listnodes(nodes:ListNode):
    string = ''
    while nodes:
        string = string + str(nodes.val) + ', '
        nodes = nodes.next

    print('[' + string[:-2] + ']')

if __name__ == '__main__':
    lists = transfer_list_to_ListNode()

    solution = Solution()
    nodes = solution.mergeKList(lists)

    print_listnodes(nodes)