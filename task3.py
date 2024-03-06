def get_longest_word(s: str) -> str:
    s = s.split(' ')
    result = max(s, key=len)
    return f'{result}'

print(get_longest_word('Python is simple and effective!'))