from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    list_tuples = []
    for i in range(len(lst) - 1):
        new_tuple = (lst[i], lst[i+1])
        list_tuples.append(new_tuple)
    return list_tuples

print(get_pairs([1,2,3,8,9]))