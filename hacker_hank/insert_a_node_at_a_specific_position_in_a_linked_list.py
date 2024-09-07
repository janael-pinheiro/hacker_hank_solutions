class SinglyLinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def insert_node_at_position(llist, data, position):
    if llist is None:
        return SinglyLinkedListNode(data)

    head = llist
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        return new_node
    index = 0
    current = head
    last = head
    while current.next is not None and index < position:
        last = current
        current = current.next
        index += 1
    last.next = new_node
    new_node.next = current
    return head


