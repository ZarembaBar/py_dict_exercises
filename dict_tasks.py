from typing import Dict, List


def convert_input_lists_into_dict(keys_list: List[str], values_list: List[int]) -> Dict[str, int]:
    converted_dictionary = {}
    for position in range(len(keys_list)):
        converted_dictionary[keys_list[position]] = values_list[position]
    return converted_dictionary


def merge_two_dicts_into_one(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


def print_value_from_nested_dict(input_dict: Dict[str, Dict[str, Dict[str, Dict[str, int]]]]) -> int:
    result = input_dict["class"]["student"]["marks"]["history"]
    return result
