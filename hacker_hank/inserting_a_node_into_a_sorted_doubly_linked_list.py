from hacker_hank.nodes import DoublyLinkedListNode


def sorted_insert(llist, data):
    if llist is None:
        return DoublyLinkedListNode(data)

    head = llist
    new_node = DoublyLinkedListNode(data)
    if data <= head.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    current = head
    last = head
    while current is not None and data >= current.data:
        last = current
        current = current.next
    last.next = new_node
    new_node.next = current
    new_node.prev = last
    if current is not None:
        current.prev = new_node
    return head
