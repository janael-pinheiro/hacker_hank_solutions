from hacker_hank.insert_a_node_at_a_specific_position_in_a_linked_list import insert_node_at_position
from pytest import mark


@mark.parametrize("nodes, data, position, expected", [
    ([1, 2, 3], 4, 2, [1, 2, 4, 3])
])
def test_insert_node_at_position(nodes, data, position, expected, build_list_nodes):
    linked_list = build_list_nodes(nodes)
    expected_list = build_list_nodes(expected)
    output = insert_node_at_position(linked_list, data, position)
    assert output.data == expected_list.data
