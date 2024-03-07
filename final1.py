from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_values = set()
    for i in lst:
        for value in i.values():
            unique_values.add(value)
    return unique_values

inpt = [{"V":"S001"}, {"V":"S0002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}]

print(check(inpt))