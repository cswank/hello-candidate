class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def create_linked_list(n):
    """Creating linked list for the given
       size"""
    linked_list = Node(1)
    head = linked_list
    for i in range(2, n):
        head.next = Node(i)
        head = head.next
    return linked_list

def print_linked_list(node):
    """To print the linked list in forward"""
    while node:
        print '[',node,']','[ref] ->',
        node = node.next
    print '-> None'

"""
Fix this method
"""
def find_middle_test(node):
    length = 1
    node_ptr = node
    while node_ptr:
        node_ptr = node_ptr.next
        length = length + 1
    length = length/2 - 1

    while node and length > 0:
        node = node.next
        length = length - 1

    return "Answer: Middle node is %s" % str(node)

node = create_linked_list(8)

print_linked_list(node)

print find_middle_test(node)


