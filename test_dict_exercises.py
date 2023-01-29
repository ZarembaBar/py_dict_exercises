from dict_tasks import convert_input_lists_into_dict, merge_two_dicts_into_one, \
    print_value_from_nested_dict, create_new_dict_from_extracted_values_of_another_dict, \
    delete_given_list_of_keys_with_their_values


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
                    "history": 80,
                    "math": 50
                }
            }
        }
    }
    assert print_value_from_nested_dict(sampleDict, "history") == 80
    assert print_value_from_nested_dict(sampleDict, "physics") == 70
    assert print_value_from_nested_dict(sampleDict, "math") == 50


def test_create_new_dict_from_extracted_values_of_another_dict_happy_path():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    assert create_new_dict_from_extracted_values_of_another_dict(sample_dict, ["name"]) == {"name": "Kelly"}
    assert create_new_dict_from_extracted_values_of_another_dict(sample_dict, ["age", "name"]) == {"age": 25,
                                                                                                   "name": "Kelly"}


def test_delete_given_list_of_keys_with_their_values_happy_path():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    assert delete_given_list_of_keys_with_their_values(sample_dict, ["name", "age"]) == {"salary": 8000,
                                                                                         "city": "New york"}


def test_delete_given_list_of_keys_with_their_values_with_empty_list_of_keys_given():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    assert delete_given_list_of_keys_with_their_values(sample_dict, []) == {"name": "Kelly",
                                                                            "age": 25,
                                                                            "salary": 8000,
                                                                            "city": "New york"}


def test_delete_given_list_of_keys_with_their_values_with_list_of_all_keys_given():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    assert delete_given_list_of_keys_with_their_values(sample_dict, ["name", "age", "salary", "city"]) == {}
