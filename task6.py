from typing import Dict

def get_dict(s: str) -> Dict[str, int]:
    dictionary = {}
    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

print(get_dict("Oh, it is python"))