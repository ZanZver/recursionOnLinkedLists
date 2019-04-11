class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

first_node = LinkedListNode(3,
    LinkedListNode(1,
        LinkedListNode(4,
            LinkedListNode(9)
        )
    )
)

def linked_list_max(node):
    if node is None:
        raise ValueError('The list is empty')
    elif node.next is None:
        return node.value
    else:
        tail_max = linked_list_max(node.next)
        return max(node.value, tail_max)

def linked_list_sum(node):
    if node is None:
        return 0
    else:
        return node.value + linked_list_sum(node.next)

def linked_list_length(node):
    if node is None:
        return 0
    else:
        return linked_list_length(node.next) + 1

print(linked_list_max(first_node))
print(linked_list_length(first_node))