from hacker_hank.insertion_sort_part_2 import insertion_sort_2


def test_insertion_sort_2(capsys):
    values_to_sort = [3, 4, 7, 5, 6, 2, 1]
    insertion_sort_2(len(values_to_sort), values_to_sort)
    expected = "3 4 7 5 6 2 1\n3 4 7 5 6 2 1\n3 4 5 7 6 2 1\n3 4 5 6 7 2 1\n2 3 4 5 6 7 1\n1 2 3 4 5 6 7\n"
    captured = capsys.readouterr()
    assert captured.out == expected
