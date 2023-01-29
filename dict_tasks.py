from typing import Any, Dict, List


def convert_input_lists_into_dict(keys_list: List[str], values_list: List[int]) -> Dict[str, int]:
    converted_dictionary = {}
    for position in range(len(keys_list)):
        converted_dictionary[keys_list[position]] = values_list[position]
    return converted_dictionary


def merge_two_dicts_into_one(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


def print_value_from_nested_dict(input_dict: Dict[str, Dict[str, Dict[str, Dict[str, int]]]], subject: str) -> int:
    result = input_dict["class"]["student"]["marks"][subject]
    return result


def create_new_dict_from_extracted_values_of_another_dict(input_dict: Dict[str, Any], keys: List[str]) -> Dict[
    str, Any]:
    new_dict = {}
    for key in keys:
        new_dict[key] = input_dict[key]
    return new_dict


def delete_given_list_of_keys_with_their_values(input_dict: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    for key in keys:
        if key in input_dict:
            input_dict.pop(key)
    return input_dict


def search_if_value_exists_in_dict(input_dict: Dict[str, int], value: int) -> str:
    list_of_values = input_dict.values()
    if value in list_of_values:
        return f"{value} present in a dict"
    else:
        return f"{value} is not in a dict"


def rename_key_of_a_dict(input_dict: Dict[str, Any]) -> Dict[str, Any]:
    input_dict["location"] = input_dict.pop("city")
    return input_dict


def display_key_of_a_min_value(input_dict: Dict[str, int]) -> str:
    for key, value in input_dict.items():
        if value == min(input_dict.values()):
            return key


def change_value_of_a_key_in_nested_dict(input_dict: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    input_dict["emp3"]["salary"] = 8500
    return input_dict
