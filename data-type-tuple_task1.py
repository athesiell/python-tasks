from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    return tuple(map(int, str(num)))

print(get_tuple(871728123))