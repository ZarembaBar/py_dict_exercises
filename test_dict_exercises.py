from two_lists_into_a_dict import convert_input_lists_into_dict


def test_convert_input_list_into_dict_happy_path():
    assert convert_input_lists_into_dict(["one", "two", "three"], [1, 2, 3]) == {"one": 1, "two": 2, "three": 3}


def test_convert_input_list_into_dict_empty_keys_list():
    assert convert_input_lists_into_dict([], [1, 2, 3]) == {}


def test_convert_input_list_into_dict_empty_values_list():
    assert convert_input_lists_into_dict(["one", "two", "three"], []) == {"one": 0, "two": 0, "three": 0}


def test_convert_input_list_into_dict_empty_both_lists():
    assert convert_input_lists_into_dict([], []) == {}


if __name__ == "__main__":
    test_convert_input_list_into_dict_happy_path()
    test_convert_input_list_into_dict_empty_keys_list()
    test_convert_input_list_into_dict_empty_values_list()
    test_convert_input_list_into_dict_empty_both_lists()
