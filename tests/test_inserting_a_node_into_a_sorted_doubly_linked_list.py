from hacker_hank.inserting_a_node_into_a_sorted_doubly_linked_list import sorted_insert
from pytest import mark


@mark.parametrize("nodes, data, expected", [
    ([1, 2, 4], 3, [1, 2, 3, 4])
])
def test_sorted_insert(nodes, data, expected, build_doubly_linked_list):
    doubly_linked_list = build_doubly_linked_list(nodes)
    expected_list = build_doubly_linked_list(expected)
    output = sorted_insert(doubly_linked_list, data)
    assert output.data == expected_list.data
