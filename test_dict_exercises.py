from dict_tasks import convert_input_lists_into_dict, merge_two_dicts_into_one, \
    print_value_from_nested_dict


def test_convert_input_list_into_dict_happy_path():
    assert convert_input_lists_into_dict(["one", "two", "three"], [1, 2, 3]) == {"one": 1, "two": 2, "three": 3}


def test_convert_input_list_into_dict_empty_keys_list():
    assert convert_input_lists_into_dict([], [1, 2, 3]) == {}


def test_convert_input_list_into_dict_empty_both_lists():
    assert convert_input_lists_into_dict([], []) == {}


def test_merge_two_dicts_into_one_happy_path():
    assert merge_two_dicts_into_one({"one": 1, "two": 2, "three": 3}, {"three": 3, "four": 4, "five": 5}) == {"one": 1,
                                                                                                              "two": 2,
                                                                                                              "three": 3,
                                                                                                              "four": 4,
                                                                                                              "five": 5}


def test_merge_two_dicts_into_one_with_the_same_dicts():
    assert merge_two_dicts_into_one({"one": 1, "two": 2}, {"one": 1, "two": 2}) == {"one": 1, "two": 2}


def test_merge_two_dicts_into_one_when_one_of_dict_is_empty():
    assert merge_two_dicts_into_one({"one": 1, "two": 2}, {}) == {"one": 1, "two": 2}
    assert merge_two_dicts_into_one({}, {"one": 1, "two": 2}) == {"one": 1, "two": 2}


def test_print_value_from_nested_dict_happy_path():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    assert print_value_from_nested_dict(sampleDict) == 80
