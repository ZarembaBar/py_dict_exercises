from typing import List, Dict


def convert_input_lists_into_dict(keys_list: List[str], values_list: List[int]) -> Dict[str, int]:
    converted_dictionary = {}
    for position in range(len(keys_list)):
        if len(values_list) == position:
            values_list.append(0)
        converted_dictionary[keys_list[position]] = values_list[position]
    return converted_dictionary

