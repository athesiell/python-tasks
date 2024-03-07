from typing import Union, List

ListType = List[Union[int, str]]

def get_fizzbuzz_list(n:int) -> ListType:
    some_list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            some_list.append('FizzBuzz')
        elif i % 3 == 0:
            some_list.append('Fizz')
        elif i % 5 == 0:
            some_list.append('Buzz')
        else:
            some_list.append(i)
    return some_list

print(get_fizzbuzz_list(15))