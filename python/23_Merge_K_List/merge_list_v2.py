from queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, value):
        return self.val < value.val

    def __gt__(self, value):
        return self.val > value.val

class Solution:
    def mergeKList(self, lists : list) -> ListNode:
        dummy_ptr = ptr = ListNode(0)
        q = PriorityQueue()

        for l in lists:
            if l:
                q.put(l)

        while not q.empty():
            minimum_node = q.get()

            ptr.next = ListNode(minimum_node.val)
            ptr = ptr.next
            
            node = minimum_node.next
            if node:
                pass
                q.put(node)

            # ptr.next = ListNode(val)
            # ptr = ptr.next

            # node = minimum_node.next
            # if node:
            #     q.put((node.val, node))
        
        return dummy_ptr.next

def transfer_list_to_ListNode():
    list_input = [[1,5,6], [1,4,9], [7,8]]
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