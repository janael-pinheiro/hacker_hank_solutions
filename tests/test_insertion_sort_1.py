from hacker_hank.insertion_sort_part_1 import insertion_sort_1


def test_insertion_sort_1(capsys):
    input_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    insertion_sort_1(len(input_values), input_values)
    expected = "2 3 4 5 6 7 8 9 10 10\n2 3 4 5 6 7 8 9 9 10\n2 3 4 5 6 7 8 8 9 10\n2 3 4 5 6 7 7 8 9 10\n2 3 4 5 6 6 7 8 9 10\n2 3 4 5 5 6 7 8 9 10\n2 3 4 4 5 6 7 8 9 10\n2 3 3 4 5 6 7 8 9 10\n2 2 3 4 5 6 7 8 9 10\n1 2 3 4 5 6 7 8 9 10\n"
    captured = capsys.readouterr()
    assert captured.out == expected

