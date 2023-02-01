from dict_tasks import convert_input_lists_into_dict, merge_two_dicts_into_one, \
    print_value_from_nested_dict, create_new_dict_from_extracted_values_of_another_dict, \
    delete_given_list_of_keys_with_their_values, search_if_value_exists_in_dict, rename_key_of_a_dict, \
    display_key_of_a_min_value, change_value_of_a_key_in_nested_dict


def test_convert_input_list_into_dict_happy_path():
    assert convert_input_lists_into_dict(["one", "two", "three"], [1, 2, 3]) == {"one": 1, "two": 2, "three": 3}


def test_convert_input_list_into_dict_if_first_list_is_shorter_the_second():
    try:
        assert convert_input_lists_into_dict([], [1, 2, 3]) == {}
    except ValueError:
        assert "Lists have to be the same lenght"


def test_convert_input_list_into_dict_if_second_ist_is_shorter_the_first():
    try:
        assert convert_input_lists_into_dict(["one", "two", "three"], []) == {}
    except ValueError:
        assert "Lists have to be the same lenght"


def test_convert_input_list_into_dict_empty_both_lists():
    assert convert_input_lists_into_dict([], []) == {}


def test_merge_two_dicts_into_one_happy_path():
    assert merge_two_dicts_into_one({"one": 1, "two": 2, "three": 3}, {"three": 3, "four": 4, "five": 5}) == {"one": 1,
                                                                                                              "two": 2,
                                                                                                              "three": 3,
                                                                                                              "four": 4,
                                                                                                              "five": 5}


def test_merge_two_dicts_into_one_with_the_same_dicts():
    assert merge_two_dicts_into_one({"one": 1, "two": 2}, {"one": 1, "two": 2}) == {"one": 1,
                                                                                    "two": 2}


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


def test_search_if_value_exists_in_dict_happy_path():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    assert search_if_value_exists_in_dict(sample_dict, 200) == "200 present in a dict"
    assert search_if_value_exists_in_dict(sample_dict, 300) == "300 present in a dict"
    assert search_if_value_exists_in_dict(sample_dict, 50) == "50 is not in a dict"


def test_rename_key_of_a_dict_happy_path():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    assert rename_key_of_a_dict(sample_dict) == {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}


def test_display_key_of_a_min_value_happy_path():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    assert display_key_of_a_min_value(sample_dict) == 'Math'


def test_change_value_of_a_key_in_nested_dict_happy_path():
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    assert change_value_of_a_key_in_nested_dict(sample_dict) == {'emp1': {'name': 'Jhon', 'salary': 7500},
                                                                 'emp2': {'name': 'Emma', 'salary': 8000},
                                                                 'emp3': {'name': 'Brad', 'salary': 8500}}
