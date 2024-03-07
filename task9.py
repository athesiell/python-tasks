from typing import List

def foo(nums: List[int]) -> List[int]:
    total = 1
    for num in nums:
        total *= num

    result = []
    for num in nums:
        result.append(total // num)
    return result

print(foo([1,2,3,4,5]))