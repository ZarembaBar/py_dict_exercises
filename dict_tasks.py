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


def create_new_dict_from_extracted_values_of_another_dict(input_dict: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    new_dict = {}
    for key in keys:
        if key in input_dict:
            new_dict.update({key: input_dict[key]})
    return new_dict
